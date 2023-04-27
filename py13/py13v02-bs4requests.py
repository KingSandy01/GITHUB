import bs4
import requests

res = requests.get('https://www.youtube.com')
    # type(res)
    # res.text

soup = bs4.BeautifulSoup(res.text, 'lxml')
    # type(soup)
titleName = soup.select('title')
print(titleName[0].getText())


