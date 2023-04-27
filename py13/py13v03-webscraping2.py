#web scrapping

import requests
import bs4

def wScrap():

    res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
    # type(res)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    soup.select('.mw-headline')

    for i in soup.select('.mw-headline'):
        print(i.text)

def main():
    wScrap()

if __name__ == '__main__':
    main()