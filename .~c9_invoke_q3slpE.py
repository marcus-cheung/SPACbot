import requests
import urllib.request
from bs4 import BeautifulSoup
from tableMaker import getTicker
import random

cookies = dict(BCPermissionLevel="PERSONAL")

ip_addresses = [
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.15.223.0:9018",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@144.168.151.176:6220",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@192.153.171.127:6200",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.8.94.140:9185",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@23.254.90.149:8189",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@104.227.76.241:6338",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.131.213.30:7578",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.8.94.100:9145",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.5.65.219:8725",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.128.245.112:9123",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.147.28.40:9098",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.152.196.111:9144",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@194.33.29.67:7651",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.27.23.222:9310",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@200.0.61.38:6113",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@84.21.188.84:8618",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.23.245.239:8810",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.5.65.49:8555",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@192.153.171.91:6164",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.94.46.121:6135",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.94.47.115:8159",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.27.10.135:6220",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.151.104.92:9144",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.131.213.71:7619",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.154.84.165:8216",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@176.116.231.110:7452",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.94.47.104:8148",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@200.0.61.249:6324",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.134.187.22:7059",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.9.122.220:8301",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.141.176.226:8791",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@185.250.39.245:8764",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.23.253.82:7654",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.8.215.118:8137",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.92.247.84:6592",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.136.228.117:6172",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.154.244.172:8210",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.142.28.66:8077",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.128.76.246:6247",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@176.116.230.96:7182",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@185.126.66.132:7648",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@176.116.231.179:7521",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@182.54.239.142:8159",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.152.202.171:9176",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@85.209.129.114:8654",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.137.40.143:8696",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.72.55.105:7142",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@2.59.21.107:7637",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@2.56.101.175:8707",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.8.215.122:8141",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@194.33.29.167:7751",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.8.231.54:9060",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@194.33.29.32:7616",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@182.54.239.156:8173",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.86.15.18:8565",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@192.166.153.119:8194",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.154.84.60:8111",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@176.116.230.136:7222",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.8.231.243:9249",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@85.209.130.81:7622",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@194.33.29.83:7667",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.137.60.210:6738",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.142.28.206:8217",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.137.80.70:9090",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@2.59.21.180:7710",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.142.28.3:8014",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.72.55.201:7238",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.94.47.81:8125",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.94.47.245:8289",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.72.55.127:7164",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.72.55.200:7237",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.142.28.58:8069",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.8.231.189:9195",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@185.99.96.151:8666",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@182.54.239.97:8114",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@2.56.101.136:8668",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.92.247.166:6674",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@185.95.157.190:6211",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.87.249.197:7775",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.8.231.47:9053",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@185.95.157.131:6152",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@85.209.130.123:7664",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@85.209.129.39:8579",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.87.249.15:7593",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.92.247.197:6705",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@2.56.101.219:8751",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@185.95.157.117:6138",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@185.95.157.31:6052",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.86.15.184:8731",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.86.15.187:8734",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@185.99.96.20:8535",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@195.158.192.80:8657",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.86.15.105:8652",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@2.56.101.35:8567",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@182.54.239.145:8162",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.92.247.141:6649",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@45.87.249.249:7827",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.151.160.57:8144",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.151.161.5:8348",
    "http://ddtkwwfb-dest:1n4d6mpv94ho@193.151.161.119:8462",
]

tickers = []


def getRandProxy():
    proxy_index = random.randint(0, len(ip_addresses) - 1)
    proxy = {"http": ip_addresses[proxy_index], "https": ip_addresses[proxy_index]}
    return proxy


latest_titles = []


def getURL(ticker):
    return (
        "https://www.google.com/search?q="
        + ticker
        + "&gl=us&hl=en&pws=0&tbm=nws&sxsrf=ALeKk02MADQALXb3n0TTjhZ4Cg26zuCUTQ:1613878744413&source=lnt&tbs=sbd:1&sa=X&ved=0ahUKEwjliZXqhvruAhXVLqYKHeWRDMkQpwUIKQ&biw=1440&bih=798&dpr=2"
    )


# called if spac track updates
def update():
    global tickers
    tickers = getTicker()
    global latest_titles
    latest_titles = generateTitles()
    print(latest_titles)


# makes list of latest titles
def generateTitles():
    print("Generating titles...")
    titles = []

    while True:
        proxy = getRandProxy()
        for x in tickers:
            url = getURL(x)
            html = requests.get(
                url,
                headers={"User-Agent": "Mozilla/5.0"},
                cookies=cookies,
                proxies=proxy,
            )

            soup = BeautifulSoup(html.text, "html.parser")

            if "unusual traffic" in soup.text or "an" in soup.text:
                print("error")
                continue
            print(soup.text)
            atag = soup.find_all("div", attrs={"class": "BNeawe vvjwJb AP7Wnd"})
            for x in atag[0:1]:
                titles.append(x.text)
        return titles


def msgMaker(title):
    return "```css" + "[" + title + "]" + "\n" + "```"


def scrape():
    global latest_titles
    newTitles = generateTitles()
    msg = ""
    for i in range(len(newTitles)):
        title = newTitles[i]
        if title != latest_titles[i]:
            msg += msgMaker(title)
    return msg
