# Gerrit van Rensburg

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv
from datetime import datetime

my_url = 'https://tradingeconomics.com/countries'

print("Hello KOR")

uClient = uReq(my_url) #Opens up the connection, and gets the webpage and load it, save it as uClient
page_html = uClient.read() #Pass Read functionand dumps all the html data in variable page_htlm
uClient.close() #close the connection
page_soup = soup(page_html, "html.parser")  #parse all the htlm that was grabbed

containers = page_soup.findAll("li", {"class": "list-group-item"})
l = (len(containers))
print(l)
print(soup.prettify(containers[1]))

#for x in range(1, l):
#    container = containers[x]
container = containers[1]
#    if (container.a["href"])
print(container.a["href"])
print(container.a)
print(container.text)
print(containers[200])
#        name = (container.a["href"])

#        with open('index.csv', 'a') as kor_csv:
#            writer = csv.writer(kor_csv)
#            writer.writerow([name, datetime.now()])
#        else x+1

print("Completed")
