#!/usr/bin/python
#-- coding: utf8 --

from urllib2 import *
import json

def banner():
    print ("\033[97m█▀█ █▀▀ █▀▀ █▀█ █▄░█   █▀▀ ▄▀█ ▀█▀\033[1;m")
    print ("\033[97m█▀▄ ██▄ █▄▄ █▄█ █░▀█   █▄▄ █▀█ ░█░\033[1;m")
    print ("\033[97m    .:.; By MishaKorzhik ;.:.\033[1;m")
def menu():
    print ("\n\033[97m1. Detect Tech\033[1;m")
    print ("\033[97m2. DNS Lookup + Cloudflare Detector\033[1;m")
    print ("\033[97m3. Zone Transfer\033[1;m")
    print ("\033[97m4. Ip Lookup\033[1;m")
    print ("\033[97m5. Cms Scanner\033[1;m")
    print ("\033[97m6. Robots.txt Scanner\033[1;m")
    print ("\033[97m7. Link Grabber\033[1;m")
def recon():
    try:
        choice = input('\033[1;91mWhile your choice:\033[1;m ')
        if choice == 1:
            print('\033[1;91mExample: google.com\033[1;m ')
            dom = raw_input('\033[1;91mWhile domain:\033[1;m ')
            d0 = 'http://api.larger.io/v1/search/key/WT7Z8YKBXKTU8AEKLERUXFW7CAXLWQFK?domain='+dom
            tech = urlopen(d0).read()
            print(tech)
            menu()
            recon()
        if choice == 2:
            domain = raw_input('\033[1;91mWhile Domain: \033[1;m')
            ns = "http://api.hackertarget.com/dnslookup/?q=" + domain
            pns = urlopen(ns).read()
            print(pns)
            if 'cloudflare' in pns:
                print("\033[1;31mCloudflare Detected!\033[1;m")
            else:
                print(")\033[1;31mNot Protected By cloudflare\033[1;m")
            menu()
            recon()
        if choice == 3:
            domain = raw_input('\033[1;91mWhile Domain: \033[1;m')
            zone = "http://api.hackertarget.com/zonetransfer/?q=" + domain
            try:
                pzone = urlopen(zone).read()
                print(pzone)
            except 'failed' in pzone:
                print("\033[1;31mZone transfer failed\033[1;m")
            menu()
            recon()
            domip = raw_input('\033[1;91mWhile Domain or IP Address: \033[1;m')
            header = "http://api.hackertarget.com/httpheaders/?q=" + domip
            pheader = urlopen(header).read()
            print(pheader)
            menu()
            recon()
        if choice == 4:
            ip = raw_input('')
            lookup = "https://api.shodan.io/dns/resolve?hostnames=" + ip + "&key=5448RQUXTLZVjInEHEn2r3JaC2prWbbd"
            l = urlopen(lookup).read()
            print(l)
            menu()
            recon()
        if choice == 5:
            print('\033[1;91mExample: google.com\033[1;m ')
            ip = raw_input('\033[1;91mWhile Domain: \033[1;m')
            cms = "https://whatcms.org/APIEndpoint/Detect?key=746f350b4b16644cd12fdb77a8ea14155c083cd3269036b30126e423ba0d7d61ffdd4f&url=" + ip
            cmss = urlopen(cms).read()
            print(cmss)
            menu()
            recon()
        if choice == 6:
            domain = raw_input('\033[1;91mEnter Domain: \033[1;m')
            if 'http://' in domain or 'https://' in domain:
                pass
            else:
                domain = 'http://' + domain
            robot = domain + "/robots.txt"
            probot = urlopen(robot).read()
            print(probot)
            menu()
            recon()
        if choice == 7:
            page = raw_input('\033[1;91mEnter URL: \033[1;m')
            if 'http://' in page or 'https://' in page:
                pass
            else:
                page = 'http://' + page
            crawl = "https://api.hackertarget.com/pagelinks/?q=" + page
            pcrawl = urlopen(crawl).read()
            print(pcrawl)
            menu()
            dog()
        else:
            print("\033[1;31m[-] Invalid option!\033[1;m")
            menu()
            recon()
    except:
        print("\033[1;31m[-] Something went wrong!\033[1;m")
        menu()
        recon()
banner()
menu()
recon()
