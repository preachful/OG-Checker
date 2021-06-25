import cloudscraper
import threading
import os
import time
from datetime import datetime
from colorama import Fore, init
from functions.utilities import title, logo
from functions.proxies import proxies_scraper, proxies_random

init(autoreset=True)

locker = threading.Lock()
request = cloudscraper.create_scraper()

date = datetime.today().strftime("%Y-%m-%d %H.%M.%S")
tocheck = []
hits = 0
bad = 0

def check(use_proxies, proxies_file, username):
	global tocheck, hits, bad

	retry = 0
	while retry <= 5:
		try:
			if use_proxies == "y":
				proxy = proxies_random(proxies_file)
			else:
				proxy = {
					"http": None,
					"https": None
				}
			response = request.post("https://accounts.api.playstation.com/api/v1/accounts/onlineIds", json={"onlineId": username, "reserveIfAvailable": False}, proxies=proxy)
			if response.status_code != 403:
				locker.acquire()
				if response.status_code == 201:
					hits += 1
					title(f"Checking - Hits: {hits}")	
					
					if not os.path.exists(f"results/Playstation/{date}"):
						os.makedirs(f"results/Playstation/{date}")
					if not os.path.isfile(f"results/Playstation/{date}/hits.txt"):
						open(f"results/Playstation/{date}/hits.txt", "w")
					with open(f"results/Playstation/{date}/hits.txt", "a") as file:
						file.write(f"{username}\n")
					
					print(f"{Fore.LIGHTGREEN_EX}[Hit] {username}")
				else:
					bad += 1
					print(f"{Fore.LIGHTRED_EX}[Bad] {username}")
				
				if len(tocheck) == hits + bad:
					title("Checking - Finished")

					logo()
					print(f"{Fore.LIGHTWHITE_EX}OG-Checker found {Fore.LIGHTGREEN_EX}{hits} {Fore.LIGHTWHITE_EX}available usernames!")
					if hits >= 1:
						print(f"{Fore.LIGHTWHITE_EX}You can find them here: results/Playstation/{date}/hits.txt")
					time.sleep(10)
				locker.release()
				break
			else:
				retry += 1
				locker.acquire()
				print(f"{Fore.LIGHTRED_EX}[Proxy Blacklisted] {username} - {proxy['http']}")
				locker.release()
		except:
			pass
	
	if retry >= 5:
		bad += 1
		if len(tocheck) == hits + bad:
			locker.acquire()
			title("Checking - Finished")

			logo()
			print(f"{Fore.LIGHTRED_EX}OG-Checker found {Fore.LIGHTGREEN_EX}{hits} {Fore.LIGHTRED_EX}available usernames!")
			if hits >= 1:
				print(f"{Fore.LIGHTRED_EX}You can find them here: {Fore.LIGHTGREEN_EX}results/Playstation/{date}/hits.txt")
			locker.release()
			time.sleep(10)

def starter(usernames_file, use_proxies, own_proxies, proxies_file, threads_amount):
	global tocheck
	
	for username in open(usernames_file):
		tocheck.append(username.rstrip())

	if use_proxies == "y":
		if own_proxies != "y":
			threading.Thread(target=proxies_scraper).start()

	title(f"Checking - Hits: {hits}")

	for username in tocheck:
		thread = threading.Thread(target=check, args=(use_proxies, proxies_file, username))
		thread.start()

		default_threads = threading.active_count()
		if threading.active_count() == threads_amount + default_threads:
			thread.join()