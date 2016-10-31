import requests
import sys
import webbrowser
from bs4 import BeautifulSoup


def search(stuff):

    print('Googling...')
    res=requests.get('http://www.google.com/search?q=' + ' '.join(stuff))

    try:
        res.raise_for_status()
    except Exception as exc:
        print("There was a problem:%s"%(exc))
    soup=BeautifulSoup(res.text)
    inPageLinks=soup.select(".r a")
    numOpen=min(5,len(inPageLinks))
    for i in range(numOpen):
        webbrowser.open("http://google.com"+inPageLinks[i].get("href"))


if __name__=="__main__":
    if len(sys.argv)<2:
        print("Enter something to search after the file name!")
    else:
        search(sys.argv[1:])



