import requests
import json
from bs4 import BeautifulSoup

def getEconomist():
    url = "https://www.economist.com/search?q=Bitcoin&page=1"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    contents = soup.find_all('div', class_='css-1ehrfcr e1k9lotg0')
    articles = []

    for content in contents:
    
        href = content.find('a').get('href')
        title = content.find('span', class_="_headline").text
        img = content.find('img').get('src')
        
        subpage = requests.get(href)
        subsoup = BeautifulSoup(subpage.content, 'html.parser')
        subcontent = subsoup.find('div', class_='layout-article-meta')

        date = subcontent.find('time').get('datetime')

        obj = {'source': "The Economist"}
        obj['href'] = href
        obj['title'] = title
        obj['img'] = img
        obj['date'] = date
        
        articles.append(obj)
    
    return articles

all_articles = {}

articles = getEconomist()

for a in articles:
    if a['date'] in all_articles:
        all_articles[a['date']].append(a)
    else:
        all_articles[a['date']] = [a]

out_file = open("articles.json", "w")
json.dump([all_articles], out_file)
out_file.close()

# print(links[0].find_all('a')[0].get('href'))

# {'title': ?, 'date': ?, img: ?, author: ?, 'href': }

