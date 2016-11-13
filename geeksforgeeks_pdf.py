import requests
import sys,os
from bs4 import BeautifulSoup

to_crawl=set()
url="http://www.geeksforgeeks.org"
re=requests.get(url)
soup=BeautifulSoup(re.text,"lxml")
crawled=set()
li=soup.find_all("a")
crawled.add(url)
for item in li:
    href=item.get("href")
    if not href:
        continue
    if href.find("amazon")>=0:
        to_crawl.add(href)
count=0

print(to_crawl)
print("yogesh")

while len(to_crawl):
    url=to_crawl.pop()
    if url not in crawled:
        count=count+1
        crawled.add(url)
        try:
            re=requests.get(url)
            print(count,url)
            soup=BeautifulSoup(re.text,"lxml")
            li=soup.find_all("a")
    
            for item in li:
                href=item.get("href")
                if not href:
                    continue
                if href.find("amazon")>=0:
                    to_crawl.add(href)
        except:
            continue
       
    else:
        continue


for item in crawled:
    print(item)

