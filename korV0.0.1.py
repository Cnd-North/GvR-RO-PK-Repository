# Gerrit van Rensburg

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv
from datetime import datetime

my_url = 'https://tradingeconomics.com/united-states/indicators'

print("Hello KOR")

uClient = uReq(my_url) #Opens up the connection, and gets the webpage and load it, save it as uClient
page_html = uClient.read() #Pass Read functionand dumps all the html data in variable page_htlm
uClient.close() #close the connection
page_soup = soup(page_html, "html.parser")  #parse all the htlm that was grabbed


overviews = page_soup.findAll("td", {"style": "padding-left: 10px; text-align: left; font-weight: 600;"})

lasts = page_soup.findAll("td", {"style": "text-align: left"})

containers = page_soup.findAll("td", {"class": "hidden-sm hidden-xs"})

l_overviews = (len(lasts))
print(l_overviews)
print(soup.prettify(overviews[0]))

l_lasts = (len(lasts))
print(l_lasts)
print(soup.prettify(lasts[0]))

l_containers = (len(containers))
print(l_containers)
print(soup.prettify(containers[1]))


overview = overviews[0]
o = overview.text.strip()
print(overview.text)
print(o)
overview = overviews[1]
print(overview.text)
last = overviews[4]
print(overview.text)

last = lasts[0]
l = (last.text)
print(last.text)
last = lasts[1]
print(last.text)
last = lasts[4]
print(last.text)

container = containers[0]
c = (container.text)
print(container.text)
container = containers[1]
print(container.text)

#containers = page_soup.findAll("li", {"class": "hidden-head"})
#l = (len(containers))
#print(l)
#print(soup.prettify(containers[1]))

#for x in range(1, l):
#    container = containers[x]
#container = containers[1]
#    if (container.a["href"])
#print(container.tr)
#print(container.td)
#print(container.a)
#print(container.text)
#print(containers[20])
#        name = (container.a["href"])

with open('index.csv', 'a') as kor_csv:
    writer = csv.writer(kor_csv)
    writer.writerow([o, datetime.now()])
    writer.writerow([l, datetime.now()])
    writer.writerow([c, datetime.now()])
#        else x+1

print("Completed")
