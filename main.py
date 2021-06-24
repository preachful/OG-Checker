import threading
import requests
import random
import time
import os
import ctypes
import cloudscraper
from colorama import Fore, init

init(autoreset=True)
title = "PSNSniper | By Goldfire | "
os.system("mode con: cols=138 lines=30")
locker = threading.Lock()

def logo():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

	print(f"""{Fore.LIGHTBLUE_EX}
                              ██▓███    ██████  ███▄    █      ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  
                             ▓██░  ██▒▒██    ▒  ██ ▀█   █    ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
                             ▓██░ ██▓▒░ ▓██▄   ▓██  ▀█ ██▒   ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
                             ▒██▄█▓▒ ▒  ▒   ██▒▓██▒  ▐▌██▒     ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
                             ▒██▒ ░  ░▒██████▒▒▒██░   ▓██░   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
                             ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
                             ░▒ ░     ░ ░▒  ░ ░░ ░░   ░ ▒░   ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
                             ░░       ░  ░  ░     ░   ░ ░    ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ 
                                            ░           ░          ░           ░  ░              ░  ░   ░     
							{Fore.LIGHTYELLOW_EX}Finding an OG Nickname has never been {Fore.LIGHTGREEN_EX}easier{Fore.LIGHTYELLOW_EX}.
	""")
	print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")

def _proxies_scraper():
	while True:
		response = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=elite&simplified=true")
		with open("proxies.txt", "wb") as file:
			file.write(response.content)

		time.sleep(300)

def _proxies_random():
	proxies_list = open(proxies_file).readlines()
	proxy = random.choice(proxies_list).rstrip()
	proxies = {
		"http": f"http://{proxy}",
		"https": f"http://{proxy}"
	}
	
	return proxies

def _check(nickname):
	global hits

	for i in range(0, 3):
		try:
			response = cloudscraper.create_scraper().post("https://accounts.api.playstation.com/api/v1/accounts/onlineIds", json={"onlineId": nickname, "reserveIfAvailable": False}, proxies=_proxies_random())
			if response.status_code != 403:
				locker.acquire()
				if response.status_code == 201:
					hits += 1
					ctypes.windll.kernel32.SetConsoleTitleW(f"{title} Hits: {hits}")	
					
					if not os.path.isfile("hits.txt"):
						open("hits.txt", "w")
					with open("hits.txt", "a") as file:
						file.write(f"{nickname}\n")
					
					print(f"{Fore.LIGHTGREEN_EX}[Hit] {nickname}")
				else:
					print(f"{Fore.LIGHTRED_EX}[Bad] {nickname}")
				locker.release()
				break
			else:
				locker.acquire()
				print(f"{Fore.LIGHTRED_EX}[Proxy Blacklisted] {_proxies_random()['http']}")
				locker.release()
		except:
			pass

def init():
	global own_proxies, proxies_file

	ctypes.windll.kernel32.SetConsoleTitleW(f"{title} Initialization")

	logo()
	print(f"{Fore.LIGHTMAGENTA_EX}Enter file where nicknames to check are located. (with .txt)")
	nicknames_file = input("\n~# ")

	logo()
	print(f"{Fore.LIGHTMAGENTA_EX}Do you want to use your own proxies? (Only HTTP(s), y/n)")
	own_proxies = input("\n~# ").lower()
	if own_proxies == "y":
		logo()
		print(f"{Fore.LIGHTMAGENTA_EX}Enter file where proxies are. (with .txt)")
		proxies_file = input("\n~# ")
	else:
		proxies_file = "proxies.txt"

	logo()
	try:
		print(f"{Fore.LIGHTMAGENTA_EX}Enter amount of threads.")
		threads_amount = int(input("\n~# "))
	except:
		logo()
		print(Fore.LIGHTRED_EX + "[Error] Invalid amount.")
		time.sleep(10)
		init()
	logo()

	thread_starter(nicknames_file, threads_amount)

def thread_starter(nickname_file, threads_amount):
	global hits

	to_check = (line.rstrip() for line in open(nickname_file))

	if own_proxies == "n":
		threading.Thread(target=_proxies_scraper).start()

	hits = 0
	ctypes.windll.kernel32.SetConsoleTitleW(f"{title} Hits: {hits}")	
	for nickname in to_check:
		thread = threading.Thread(target=_check, args=(nickname,))
		thread.start()

		if threading.active_count() == threads_amount:
			thread.join()

if __name__ == "__main__":
	try:
		init()
	except KeyboardInterrupt:
		exit()