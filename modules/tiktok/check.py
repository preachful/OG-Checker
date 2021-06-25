import threading
import os
import requests
from colorama import Fore, init
from functions.utilities import title, logo
from functions.proxies import proxies_scraper, proxies_random

init(autoreset=True)

locker = threading.Lock()

def check(use_proxies, proxies_file, username):
	global hits

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
				
				if not os.path.exists(f"results/TikTok"):
					os.makedirs(f"results/TikTok")
				if not os.path.isfile("results/TikTok/hits.txt"):
					open("results/TikTok/hits.txt", "w")
				with open("results/TikTok/hits.txt", "a") as file:
					file.write(f"{username}\n")
				
				print(f"{Fore.LIGHTGREEN_EX}[Hit] {username}")
			else:
				print(f"{Fore.LIGHTRED_EX}[Bad] {username}")
			locker.release()
			break
		except:
			pass

def starter(usernames_file, use_proxies, own_proxies, proxies_file, threads_amount):
	global hits

	to_check = (line.rstrip() for line in open(usernames_file))

	if use_proxies == "y":
		if own_proxies != "y":
			threading.Thread(target=proxies_scraper).start()

	hits = 0
	title(f"Checking - Hits: {hits}")

	for username in to_check:
		thread = threading.Thread(target=check, args=(use_proxies, proxies_file, username))
		thread.start()

		default_threads = threading.active_count()
		if threading.active_count() == threads_amount + default_threads:
			thread.join()