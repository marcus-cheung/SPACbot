import requests
from urllib.request import urlopen
import lxml
from bs4 import BeautifulSoup
import redditDD as rdd
import redditTalk as rT

cookies = dict(BCPermissionLevel="PERSONAL")

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
}

# gets URL for sheet from spactrack.com
def getURL(int):
    allofit = "https://sheet2site-staging.herokuapp.com/api/v3/load_more.php/?key=1F7gLiGZP_F4tZgQXgEhsHMqlgqdSds3vO0-4hoL6ROQ&template=Table%20Template&filter=&search=&e=1&is_filter_multi=true&length=99&page="
    searching = "https://sheet2site-staging.herokuapp.com/api/v3/load_more.php/?key=1F7gLiGZP_F4tZgQXgEhsHMqlgqdSds3vO0-4hoL6ROQ&template=Table Template&filter=searching&search=&e=1&is_filter_multi=true&length=99&page="
    return searching + str(int)


# generates list of trs
def getListRows():
    index = 0
    trs = []
    while index <= 5:
        url = getURL(index)
        html = requests.get(url, headers=headers, cookies=cookies)
        soup = BeautifulSoup(html.text, "lxml")
        index += 1
        for tr in soup.find_all("tr")[2:]:
            trs.append(tr)
    return trs


tickerlist = []


def makeTable():
    list_trs = getListRows()
    table = []
    for x in list_trs:
        row = []
        index = 0
        # make each row
        while index <= 21:
            tds = x.find_all("td")
            row.append(tds[index].text)

            # add ticker to ticker list
            global tickerlist
            tickerlist.append(tds[0].text)

            index += 1
        # add rating
        rating = rate(tds[21].text)
        row.append(rating)
        
        #get upvotes for DD
        upvote = rdd.getScore(tds[0].text)
        row.append(upvote)
        
        #get upvotes for general reddit talk
        upvote = rT.getScore(tds[0].text)
        
        # add row to table
        table.append(row)
    return table


def rate(tags):
    rating = 0
    if tags.find("$500M+ Trust") >= 0:
        rating += 10000
    return rating


def getTicker():
    return tickerlist


# super update, returns True if update required
def update():
    global tickerlist
    list_trs = getListRows()
    newTicker = []
    for x in list_trs:
        tds = x.find_all("td")
        newTicker.append(tds[0].text)
    if newTicker != tickerlist:
        tickerlist = newTicker
        return True
    else:
        return False