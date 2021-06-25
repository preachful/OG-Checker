import os
from functions.utilities import title, logo
from modules.playstation.init import playstation
from colorama import Fore, init

init(autoreset=True)
os.system("mode con: cols=138 lines=30")

def module_choice():
	title("Module Choice")

	logo()
	print(f"{Fore.LIGHTGREEN_EX}[1] Playstation")
	choice = input("\n~# ")
	if choice == "1":
		playstation()
	else:
		module_choice()

if __name__ == "__main__":
	try:
		module_choice()
	except KeyboardInterrupt:
		exit()