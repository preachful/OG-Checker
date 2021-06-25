import os
from modules.playstation.init import playstation
from colorama import Fore, init

init(autoreset=True)
os.system("mode con: cols=138 lines=30")

if __name__ == "__main__":
	try:
		playstation()
	except KeyboardInterrupt:
		exit()