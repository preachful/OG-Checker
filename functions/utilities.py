import ctypes
import os
from colorama import Fore, init

init(autoreset=True)

def title(text):
    ctypes.windll.kernel32.SetConsoleTitleW(f"OG-Checker | By Goldfire | {text}")

def logo():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

	print(f"""{Fore.LIGHTBLUE_EX}
                              ██████╗  ██████╗        ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
                             ██╔═══██╗██╔════╝       ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
                             ██║   ██║██║  ███╗█████╗██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
                             ██║   ██║██║   ██║╚════╝██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
                             ╚██████╔╝╚██████╔╝      ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
                              ╚═════╝  ╚═════╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
							{Fore.LIGHTYELLOW_EX}Finding an OG Username has never been {Fore.LIGHTGREEN_EX}easier{Fore.LIGHTYELLOW_EX}.
	""")
	print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")