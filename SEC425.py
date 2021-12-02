import requests
import urllib.request
from bs4 import BeautifulSoup
import tableMaker

# Bypass cookies message
cookies = dict(BCPermissionLevel="PERSONAL")

ticker = tableMaker.getTicker()

# called if spac track changes
def update():
    global ticker
    ticker = tableMaker.getTicker()


def checker_425(ticker):
    # Construct SEC URL
    url = "https://sec.report/Ticker/" + ticker
    # Connect to url and convert to html
    html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies)
    # Parse and format
    soup = BeautifulSoup(html.text, "html.parser")
    # Convert page into text
    str = soup.get_text()
    if "Merger Prospectus/Communication" in str:
        return True
    return False


def msg425():
    msg = ""
    i = 0
    while i < len(ticker):
        if checker_425(ticker[i]) == True:
            msg += (
                "@here```css\n"
                + " 425 filed for "
                + "["
                + ticker[i]
                + "]"
                + "!"
                + "```"
                + "https://finance.yahoo.com/quote/"
                + ticker[i]
                + "\n"
            )
        i += 1
    return msg
