from colorama import Fore
import time
import requests
import os
from platform import system
import keyboard

banner = """ ██▓ ██▓███      ██▓     ██▓ ██▒   █▓▓█████ 
▓██▒▓██░  ██▒   ▓██▒    ▓██▒▓██░   █▒▓█   ▀ 
▒██▒▓██░ ██▓▒   ▒██░    ▒██▒ ▓██  █▒░▒███   
░██░▒██▄█▓▒ ▒   ▒██░    ░██░  ▒██ █░░▒▓█  ▄ 
░██░▒██▒ ░  ░   ░██████▒░██░   ▒▀█░  ░▒████▒
░▓  ▒▓▒░ ░  ░   ░ ▒░▓  ░░▓     ░ ▐░  ░░ ▒░ ░
 ▒ ░░▒ ░        ░ ░ ▒  ░ ▒ ░   ░ ░░   ░ ░  ░
 ▒ ░░░            ░ ░    ▒ ░     ░░     ░   
 ░                  ░  ░ ░        ░     ░  ░
                                 ░          
                                 
[!] The creator of this tool is not responsible for any damage caused by it; this tool was created for educational purposes!"""

sys = system()

def vsac(sys):
    if sys == "Windows":
        os.system('cls')
    elif sys == "Linux":
        os.system("clear")
    else:
        os.system('cls')

def iplookup(ip, timeout):
    while True:
        print(Fore.LIGHTRED_EX + banner)
        try:
            r = requests.get(f"https://ipinfo.io/{ip}/json")
            if r.status_code == 200:
                data = r.json()
                print(Fore.RESET + f"""\nIP: {ip}
Hostname: {data['hostname']}
City: {data['city']}
Region: {data['region']}
Country: {data['country']}
Loc: {data['loc']}
Org.: {data['postal']}
Timezone: {data['timezone']}""")
            else:
                print(Fore.RED + f"\n[!] Error while lookuping IP.\n" + Fore.RESET)
        except requests.RequestException as e:
            print(Fore.RED + f"[!] Error: {e}")

        if keyboard.is_pressed('q'):
            print("[!] Exiting...")
            break
        time.sleep(timeout)
        vsac(sys)

def menu():
    vsac(sys)
    print(Fore.LIGHTRED_EX + f"{banner}" + Fore.RESET)
    ip = input(Fore.LIGHTRED_EX + "[" + Fore.WHITE + "+" + Fore.LIGHTRED_EX + "]" + Fore.RESET + " Insert IP: ")
    print("")
    t = int(input(Fore.LIGHTRED_EX + "[" + Fore.WHITE + "+" + Fore.LIGHTRED_EX + "]" + Fore.RESET + " Insert Timeout (Ex.: 1.5): "))
    print("")
    print(Fore.WHITE + "[!] Press 'q' to stop the tool!\n")
    time.sleep(4)
    iplookup(ip, t)

menu()
