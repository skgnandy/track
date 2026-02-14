#!/usr/bin/env python3
# << CODE BY HUNX04 (Improved Version)
# << Enhanced with better error handling, improved UI, and additional features

# IMPORT MODULE
import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

# Color Variables
Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'
Reset = '\033[0m'


# Decorator for attaching run_banner to a function
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)
    return wrapper


# FUNCTIONS FOR MENU
@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")
    print()
    print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
    
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}", timeout=10)
        req_api.raise_for_status()
        ip_data = json.loads(req_api.text)
        
        # Check if API returned an error
        if not ip_data.get('success', True):
            print(f"{Re}\n Error: {ip_data.get('message', 'Invalid IP address')}")
            return
        
        time.sleep(1)
        print(f"{Wh}\n IP target       :{Gr}", ip)
        print(f"{Wh} Type IP         :{Gr}", ip_data.get("type", "N/A"))
        print(f"{Wh} Country         :{Gr}", ip_data.get("country", "N/A"))
        print(f"{Wh} Country Code    :{Gr}", ip_data.get("country_code", "N/A"))
        print(f"{Wh} City            :{Gr}", ip_data.get("city", "N/A"))
        print(f"{Wh} Continent       :{Gr}", ip_data.get("continent", "N/A"))
        print(f"{Wh} Continent Code  :{Gr}", ip_data.get("continent_code", "N/A"))
        print(f"{Wh} Region          :{Gr}", ip_data.get("region", "N/A"))
        print(f"{Wh} Region Code     :{Gr}", ip_data.get("region_code", "N/A"))
        print(f"{Wh} Latitude        :{Gr}", ip_data.get("latitude", "N/A"))
        print(f"{Wh} Longitude       :{Gr}", ip_data.get("longitude", "N/A"))
        
        # Fixed: Better handling of coordinates
        if ip_data.get('latitude') and ip_data.get('longitude'):
            lat = ip_data['latitude']
            lon = ip_data['longitude']
            print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
        
        print(f"{Wh} EU              :{Gr}", ip_data.get("is_eu", "N/A"))
        print(f"{Wh} Postal          :{Gr}", ip_data.get("postal", "N/A"))
        print(f"{Wh} Calling Code    :{Gr}", ip_data.get("calling_code", "N/A"))
        print(f"{Wh} Capital         :{Gr}", ip_data.get("capital", "N/A"))
        print(f"{Wh} Borders         :{Gr}", ip_data.get("borders", "N/A"))
        
        # Safe access to nested dictionaries
        if "flag" in ip_data and "emoji" in ip_data["flag"]:
            print(f"{Wh} Country Flag    :{Gr}", ip_data["flag"]["emoji"])
        
        if "connection" in ip_data:
            print(f"{Wh} ASN             :{Gr}", ip_data["connection"].get("asn", "N/A"))
            print(f"{Wh} ORG             :{Gr}", ip_data["connection"].get("org", "N/A"))
            print(f"{Wh} ISP             :{Gr}", ip_data["connection"].get("isp", "N/A"))
            print(f"{Wh} Domain          :{Gr}", ip_data["connection"].get("domain", "N/A"))
        
        if "timezone" in ip_data:
            print(f"{Wh} ID              :{Gr}", ip_data["timezone"].get("id", "N/A"))
            print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"].get("abbr", "N/A"))
            print(f"{Wh} DST             :{Gr}", ip_data["timezone"].get("is_dst", "N/A"))
            print(f"{Wh} Offset          :{Gr}", ip_data["timezone"].get("offset", "N/A"))
            print(f"{Wh} UTC             :{Gr}", ip_data["timezone"].get("utc", "N/A"))
            print(f"{Wh} Current Time    :{Gr}", ip_data["timezone"].get("current_time", "N/A"))
            
    except requests.exceptions.RequestException as e:
        print(f"{Re}\n Error connecting to API: {e}")
    except json.JSONDecodeError:
        print(f"{Re}\n Error parsing API response")
    except Exception as e:
        print(f"{Re}\n Unexpected error: {e}")


@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}Enter phone number target {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}")
    default_region = "ID"

    try:
        parsed_number = phonenumbers.parse(User_phone, default_region)
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                    with_formatting=True)
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
        print(f"\n {Wh}Location             :{Gr} {location}")
        print(f" {Wh}Region Code          :{Gr} {region_code}")
        print(f" {Wh}Timezone             :{Gr} {timezoneF}")
        print(f" {Wh}Operator             :{Gr} {jenis_provider if jenis_provider else 'Unknown'}")
        print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
        print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
        print(f" {Wh}International format :{Gr} {formatted_number}")
        print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
        print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
        print(
            f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
        print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
        
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f" {Wh}Type                 :{Gr} This is a mobile number")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
        else:
            print(f" {Wh}Type                 :{Gr} This is another type of number")
            
    except phonenumbers.NumberParseException as e:
        print(f"{Re}\n Error parsing phone number: {e}")
    except Exception as e:
        print(f"{Re}\n Unexpected error: {e}")


@is_option
def TrackLu():
    try:
        username = input(f"\n {Wh}Enter Username : {Gr}")
        results = {}
        social_media = [
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.twitter.com/{}", "name": "Twitter"},
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
            {"url": "https://www.tumblr.com/{}", "name": "Tumblr"},
            {"url": "https://www.youtube.com/@{}", "name": "Youtube"},
            {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
            {"url": "https://www.snapchat.com/add/{}", "name": "Snapchat"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://www.behance.net/{}", "name": "Behance"},
            {"url": "https://www.medium.com/@{}", "name": "Medium"},
            {"url": "https://www.quora.com/profile/{}", "name": "Quora"},
            {"url": "https://www.flickr.com/people/{}", "name": "Flickr"},
            {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
            {"url": "https://www.dribbble.com/{}", "name": "Dribbble"},
            {"url": "https://www.producthunt.com/@{}", "name": "Product Hunt"},
            {"url": "https://t.me/{}", "name": "Telegram"},
            {"url": "https://weheartit.com/{}", "name": "We Heart It"},
            {"url": "https://www.reddit.com/user/{}", "name": "Reddit"},
            {"url": "https://www.spotify.com/user/{}", "name": "Spotify"}
        ]
        
        print(f"\n {Wh}========== {Gr}SEARCHING USERNAME {Wh}==========")
        print(f" {Wh}Checking {Gr}{len(social_media)}{Wh} platforms...\n")
        
        found_count = 0
        for site in social_media:
            url = site['url'].format(username)
            try:
                response = requests.get(url, timeout=5, allow_redirects=True)
                if response.status_code == 200:
                    results[site['name']] = url
                    found_count += 1
                    print(f" {Wh}[{Gr}✓{Wh}] Found on {Gr}{site['name']}")
                else:
                    results[site['name']] = f"{Ye}Not found"
            except requests.exceptions.RequestException:
                results[site['name']] = f"{Re}Error checking"
                
    except Exception as e:
        print(f"{Re}Error : {e}")
        return

    print(f"\n {Wh}========== {Gr}RESULTS ({found_count} found) {Wh}==========\n")
    for site, url in results.items():
        if "http" in str(url):
            print(f" {Wh}[{Gr}+{Wh}] {site:20} : {Gr}{url}")
        else:
            print(f" {Wh}[{Ye}-{Wh}] {site:20} : {url}")


@is_option
def showIP():
    try:
        response = requests.get('https://api.ipify.org/', timeout=5)
        Show_IP = response.text
        
        print(f"\n {Wh}========== {Gr}SHOW YOUR IP ADDRESS {Wh}==========")
        print(f"\n {Wh}[{Gr}+{Wh}] Your IP Address : {Gr}{Show_IP}")
        print(f"\n {Wh}==============================================")
    except requests.exceptions.RequestException as e:
        print(f"{Re}\n Error getting IP address: {e}")


# OPTIONS
options = [
    {
        'num': 1,
        'text': 'IP Tracker',
        'func': IP_Track
    },
    {
        'num': 2,
        'text': 'Show Your IP',
        'func': showIP
    },
    {
        'num': 3,
        'text': 'Phone Number Tracker',
        'func': phoneGW
    },
    {
        'num': 4,
        'text': 'Username Tracker',
        'func': TrackLu
    },
    {
        'num': 0,
        'text': 'Exit',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[{Gr}+{Wh}] {Gr}Press enter to continue')
        main()
    except ValueError as e:
        print(f'{Re}{e}')
        time.sleep(2)
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[{Re}!{Wh}] {Re}Exiting...{Reset}')
        time.sleep(1)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[{Gr} {opt["num"]} {Wh}] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def option():
    # BANNER TOOLS
    clear()
    stderr.writelines(f"""
████████╗██████╗  █████╗  ██████╗ ██╗  ██╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝ ██║ ██╔╝
   ██║   ██████╔╝███████║██║      █████╔╝ 
   ██║   ██╔══██╗██╔══██║██║      ██╔═██╗ 
   ██║   ██║  ██║██║  ██║╚██████╔╝██║  ██╔
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝

              {Wh}[ + ]  C O D E   B Y  S A I  [ + ]
              {Cy}[Improved Version with Enhanced Features]
    """)

    stderr.writelines(f"\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(0.5)
    stderr.writelines(f"""{Wh}
        ▄▄▄▄▄▄▄▄▄▄▄▄▄
      ▄█  ▄▄     ▄▄  █▄
     █   ▀▀        ▀▀   █
     █      ▄████▄      █
     █     █  ▄▄▄  █     █
      ▀▄    ▀████▀    ▄▀
         ▀▄▄▄▄▄▄▄▄▄▄▄▄▀

   -----------------------------
      TRACKER - TOOL
        CODE BY SAI
   -----------------------------
{Reset}
        """)
    time.sleep(0.5)


def main():
    clear()
    option()
    time.sleep(0.5)
    try:
        opt = int(input(f"{Wh}\n [{Gr}+{Wh}] {Gr}Select Option : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f'\n{Wh}[{Re}!{Wh}] {Re}Please input a valid number')
        time.sleep(2)
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[{Re}!{Wh}] {Re}Exiting...{Reset}')
        time.sleep(1)
        exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[{Re}!{Wh}] {Re}Exiting...{Reset}')
        time.sleep(1)
        exit()
