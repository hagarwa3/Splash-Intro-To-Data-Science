import urllib2
from bs4 import BeautifulSoup
m=0

#now call alchemy api on given url "http://www.insidermonkey.com/blog/hedge-funds-are-piling-into-these-dividend-stocks-part-i-340042/"
ur='http://access.alchemyapi.com/calls/url/URLGetTextSentiment?apikey=9b61009a54069badce0cc7ed6bc3f229b07d150a&url=http://www.insidermonkey.com/blog/hedge-funds-are-piling-into-these-dividend-stocks-part-i-340042/'
for i in (0, 1000):
    dat=urllib2.urlopen(ur)             #open and get html from url
    sou=BeautifulSoup(dat)              #run Beautiful Soup Implementation on html
    if sou.find('score')!=None:
        m+=float(sou.find('score').string)
    print m