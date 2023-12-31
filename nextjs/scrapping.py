import requests
from bs4 import BeautifulSoup

URL = "https://nextjs.org/blog"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")

articles = soup.find_all('article')

for article in articles:
    date = article.find('p', class_='text_wrapper__i87JK').get_text()
    title = article.find('a', class_='blog_title__eH3aB').get_text()
    content = article.find('div', class_='prose prose-vercel blog_prose__AcmB0').get_text()
    print(date)
    print(title)
    print(content)
    link = article.find('ul')
    if link:
        items = link.find_all('li')
        for i in items:
            print(f"-",i.get_text())
    print("\n")