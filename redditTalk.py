import requests
import urllib.request
from bs4 import BeautifulSoup

cookies = dict(BCPermissionLevel="PERSONAL")

def getURL(keyword):
    return 'https://www.reddit.com/r/SPACs/search/?q=' + keyword + '&source=recent&restrict_sr=1&sort=top'

def getScore(keyword):
    url = getURL(keyword)
    html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies)
    soup = BeautifulSoup(html.text, "html.parser")
    score = 0
    div = soup.find_all('div',attrs={'style':'color:#878A8C;cursor:pointer;fill:#878A8C'})
    for x in div:
        xstr = str(x)
        xtext = x.text
        if xtext.lower().find(keyword.lower())>=0:
            indexstart = xstr.find('color:#1A1A1B">')
            strshort = xstr[indexstart+15:]
            indexend = strshort.find('<')
            upvote =  str(strshort[0:indexend])
            k = upvote.find('k')
            if k != -1:
                upvote = float(upvote[0:k])*1000
            score += int(upvote)
    return score
print(getScore('lucid'))