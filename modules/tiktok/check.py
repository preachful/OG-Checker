import threading
import os
import requests
import time
from datetime import datetime
from colorama import Fore, init
from functions.utilities import title, logo
from functions.proxies import proxies_scraper, proxies_random

init(autoreset=True)

locker = threading.Lock()

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
			response = requests.head(f"https://www.tiktok.com/@{username}", proxies=proxy)
			locker.acquire()
			if response.status_code == 200:
				hits += 1
				title(f"Checking - Hits: {hits}")	
				
				if not os.path.exists(f"results/TikTok/{date}"):
					os.makedirs(f"results/TikTok/{date}")
				if not os.path.isfile(f"results/TikTok/{date}/hits.txt"):
					open(f"results/TikTok/{date}/hits.txt", "w")
				with open(f"results/TikTok/{date}/hits.txt", "a") as file:
					file.write(f"{username}\n")
				
				print(f"{Fore.LIGHTGREEN_EX}[Hit] {username}")
			else:
				bad += 1
				print(f"{Fore.LIGHTRED_EX}[Bad] {username}")

			if len(tocheck) == hits + bad:
				title("Checking - Finished")

				logo()
				print(f"{Fore.LIGHTRED_EX}OG-Checker found {Fore.LIGHTGREEN_EX}{hits} {Fore.LIGHTRED_EX}available usernames!")
				if hits >= 1:
					print(f"{Fore.LIGHTRED_EX}You can find them here: {Fore.LIGHTGREEN_EX}results/TikTok/{date}/hits.txt")
				time.sleep(10)
			locker.release()
			break
		except:
			pass
	else:
		bad += 1

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