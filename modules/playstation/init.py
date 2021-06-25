import time
from functions.utilities import title, logo
from modules.playstation.check import starter
from colorama import Fore, init

init(autoreset=True)

def playstation():
	title("Initialization")

	logo()
	print(f"{Fore.LIGHTMAGENTA_EX}Enter file where usernames to check are located. (with .txt)")
	usernames_file = input("\n~# ")

	logo()
	print(f"{Fore.LIGHTMAGENTA_EX}Do you want to use your own proxies? (Only HTTP(s), y/n)")
	own_proxies = input("\n~# ").lower()
	if own_proxies == "y":
		logo()
		print(f"{Fore.LIGHTMAGENTA_EX}Enter file where proxies are located. (with .txt)")
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

	starter(usernames_file, own_proxies, proxies_file, threads_amount)