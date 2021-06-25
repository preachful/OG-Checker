import requests
import random
import time

def proxies_scraper():
	while True:
		response = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=elite&simplified=true")
		with open("proxies.txt", "wb") as file:
			file.write(response.content)
		
		time.sleep(300)

def proxies_random(proxies_file):
	proxies_list = open(proxies_file).readlines()
	proxy = random.choice(proxies_list).rstrip()
	proxies = {
		"http": f"http://{proxy}",
		"https": f"http://{proxy}"
	}
	
	return proxies