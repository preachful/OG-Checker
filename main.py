import os
from colorama import Fore, init
from functions.utilities import title, logo
from modules.playstation.init import playstation
from modules.tiktok.init import tiktok

init(autoreset=True)
os.system("mode con: cols=138 lines=30")

def module_choice():
	title("Module Choice")

	logo()
	print(f"{Fore.LIGHTGREEN_EX}[1] Playstation             [2] TikTok")
	choice = input("\n~# ")
	if choice == "1":
		playstation()
	elif choice == "2":
		tiktok()
	else:
		module_choice()

if __name__ == "__main__":
	try:
		module_choice()
	except KeyboardInterrupt:
		exit()