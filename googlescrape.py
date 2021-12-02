import requests
import urllib.request
from bs4 import BeautifulSoup
from tableMaker import getTicker
import random
import shelve

cookies = dict(BCPermissionLevel="PERSONAL")

proxies = shelve.open('proxy.db')
ip_addresses = proxies['proxy']
proxies.close()

tickers = []
latest_titles = []

def removeProxy(proxy_dict):
    proxies = shelve.open('proxy.db')
    for ip in ip_addresses:
        if proxy_dict['http'] == ip:
            ip_addresses.remove(ip)
    proxies['proxy'] = ip_addresses
    proxies.close()


def getRandProxy():
    proxy_index = random.randint(0, len(ip_addresses) - 1)
    proxy = {"http": ip_addresses[proxy_index], "https": ip_addresses[proxy_index]}
    return proxy


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


proxy = getRandProxy()

# makes list of latest titles
def generateTitles():
    print("Generating titles...")
    titles = []
    global proxy
    index = 0
    while index < len(tickers):
        url = getURL(tickers[index])
        html = requests.get(
            url, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies, proxies=proxy
        )

        soup = BeautifulSoup(html.text, "html.parser")

        if "unusual traffic" in soup.text:
            print("Detected Robot")
            proxy = getRandProxy()
            continue
        elif "Your client does not have permission" in soup.text:
            print("403 Blocked")
            removeProxy(proxy)
            proxy = getRandProxy()
            continue

        atag = soup.find_all("div", attrs={"class": "BNeawe vvjwJb AP7Wnd"})
        for x in atag[0:1]:
            titles.append(x.text)
        index += 1
    return titles


def msgMaker(title, ticker):
    return "```css\n" + "[" + ticker + "]" + '\n"' + title + '"\n```'


def scrape():
    global latest_titles
    global tickers
    newTitles = generateTitles()
    msg = "@here"
    i = 0
    while i < len(newTitles):
        title = newTitles[i]
        if title != latest_titles[i] and title.find("merge") >= 0:
            msg += msgMaker(title, tickers[i])
    latest_titles = newTitles
    return msg


if __name__ == "__main__":
    update()
