#!/usr/bin/python3
import json, requests

def banner():
    print("\033[97m█▀█ █▀▀ █▀▀ █▀█ █▄░█   █▀▀ ▄▀█ ▀█▀\033[0;m")
    print("\033[97m█▀▄ ██▄ █▄▄ █▄█ █░▀█   █▄▄ █▀█ ░█░\033[0;m")
    print("\033[97m    .:.: By MishaKorzhik :.:.\033[0;m")

def menu():
    print("\n\033[97m1. Detect Tech\033[0;m")
    print("\033[97m2. DNS Lookup\033[0;m")
    print("\033[97m3. Zone Transfer\033[0;m")
    print("\033[97m4. Http headers\033[0;m")
    print("\033[97m5. Port Scanner\033[0;m")
    print("\033[97m6. Cms Scanner\033[0;m")
    print("\033[97m7. Robots.txt Scanner\033[0;m")
    print("\033[97m8. Link Grabber\033[0;m")

def recon():
    try:
        choice = input('\033[1;91mEnter your choice:\033[0;m ')
        if choice == "1":
            domain = input('\033[1;91mEnter Domain (ex. google.com):\033[0;m ')
            get = requests.get('http://api.larger.io/v1/search/key/WT7Z8YKBXKTU8AEKLERUXFW7CAXLWQFK?domain=' + domain).text
            print(get)
        elif choice == "2":
            domain = input('\033[1;91mEnter Domain (ex. google.com): \033[0;m')
            get = requests.get("http://api.hackertarget.com/dnslookup/?q=" + domain).text
            print(get)
            if 'cloudflare' in pns:
                print("\033[1;31mCloudflare Detected!\033[0;m")
            else:
                print(")\033[1;31mNot Protected By cloudflare\033[0;m")
        elif choice == "3":
            domain = input('\033[1;91mEnter Domain (ex. google.com): \033[0;m')
            get = requests.get("http://api.hackertarget.com/zonetransfer/?q=" + domain).text
            if "failed" in get:
                print("\033[1;31mZone transfer failed\033[0;m")
            else:
                print(get)
        elif choice == "4":
            domain = input('\033[1;91mEnter Domain (ex. google.com): \033[0;m')
            get = requests.get("http://api.hackertarget.com/httpheaders/?q=" + domain).text
            print(get)
        elif choice == "5":
            ip = input('\033[1;91mEnter IP: \033[1m')
            get = requests.get("https://internetdb.shodan.io/" + ip).json()
            h = ""
            p = ""
            v = ""
            for st in get["hostnames"]:
                h = h + ", "+str(st)
            for st in get["ports"]:
                p = p + ", "+str(st)
            for st in get["vulns"]:
                v = v + ", "+str(st)
            h = h.replace(",", "", 1)
            p = p.replace(",", "", 1)
            v = v.replace(",", "", 1)
            print("Hostnames    : "+h)
            print("Latest Ports : "+p)
            print("Vulners      : "+v)
        elif choice == "6":
            print('\033[1;91mExample: google.com\033[0;m ')
            ip = input('\033[1;91mEnter Domain (ex. google.com): \033[0;m')
            get = requests.get("https://whatcms.org/APIEndpoint/Detect?key=746f350b4b16644cd12fdb77a8ea14155c083cd3269036b30126e423ba0d7d61ffdd4f&url="+ip).text
            print(get)
        elif choice == "7":
            domain = input('\033[1;91mEnter Domain (ex. google.com): \033[0;m')
            if 'http://' in domain or 'https://' in domain:
                pass
            else:
                domain = 'http://' + domain
            get = requests.get(domain + "/robots.txt").text
            print(get)
        elif choice == "8":
            page = input('\033[1;91mEnter Domain (ex. google.com): \033[0;m')
            if 'http://' in page or 'https://' in page:
                pass
            else:
                page = 'http://' + page
            get = requests.get("https://api.hackertarget.com/pagelinks/?q=" + page).text
            print(get)
            menu()
        else:
            print("\033[1;31m[-] Invalid option!\033[0;m")
    except:
        print("\033[1;31m[-] Something went wrong!\033[0;m")
banner()
menu()
recon()
