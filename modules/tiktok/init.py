import time
from colorama import Fore, init
from functions.utilities import title, logo
from modules.tiktok.check import starter

init(autoreset=True)

def tiktok():
	title("TikTok - Initialization")

	logo()
	print(f"{Fore.LIGHTMAGENTA_EX}Enter file where usernames to check are located. (with .txt)")
	usernames_file = input("\n~# ")

	logo()
	print(f"{Fore.LIGHTMAGENTA_EX}Do you want to use proxies? (y/n)")
	use_proxies = input("\n~# ").lower()
	if use_proxies == "y":
		logo()
		print(f"{Fore.LIGHTMAGENTA_EX}Do you want to use your own proxies? (Only HTTP(s), y/n)")
		own_proxies = input("\n~# ").lower()
		if own_proxies == "y":
			logo()
			print(f"{Fore.LIGHTMAGENTA_EX}Enter file where proxies are located. (with .txt)")
			proxies_file = input("\n~# ")
		else:
			proxies_file = "proxies.txt"
	else:
		own_proxies  = "n"
		proxies_file = None

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

	starter(usernames_file, use_proxies, own_proxies, proxies_file, threads_amount)