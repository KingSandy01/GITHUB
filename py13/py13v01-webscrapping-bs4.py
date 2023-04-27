
from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.youtube.com/index.html"
    res = requests.get(url)
    html_doc = url
    soup = BeautifulSoup(html_doc, 'html.parser')

    print(soup.prettify())

    for link in soup.find_all('a'):
        print(link.get('href'))

    print(soup.get_text())

if __name__ == '__main__':
    main()

