import requests
import json
from bs4 import BeautifulSoup

def getEconomist():

    total_page = 10
    for page in range(1, total_page+1):
        url = "https://www.economist.com/search?q=Bitcoin&page=" + str(page+1)
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
            obj['date'] = date[:10]
            
            articles.append(obj)
    
    return articles

def getNewsBitcoin():

    total_page = 1512

    for num_page in range(1, total_page+1):
        url = "https://news.bitcoin.com/page/" + str(num_page) + "/?s=bitcoin"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        contents = soup.find_all('div', class_='td_module_16 td_module_wrap td-animation-stack')
        articles = []

        for content in contents:
        
            href = content.find('a').get('href')
            title = content.find('h3', class_="entry-title td-module-title").text
            img = content.find('img').get('src')
            date = content.find('time').get('datetime')

            obj = {'source': "Bitcoin.com"}
            obj['href'] = href
            obj['title'] = title
            obj['img'] = img
            obj['date'] = date[:10]
            
            articles.append(obj)
        
        if num_page % 100 == 0:
            print("news.bitcoin.com " + str(num_page) + " pages done!")
    
    return articles

def getMarketWatch():

    total_page = 3

    for num_page in range(1, total_page+1):
        url = "https://www.marketwatch.com/search?q=bitcoin&Link=MW_SearchAC&mod=keyword_search&mp=806&o=" + str(num_page*15 + 1)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        contents = soup.find_all('div', class_='searchresult')
        meta = soup.find_all('div', class_='deemphasized')
        articles = []

        for i in range(len(contents)):
            a_tag = contents[i].find('a')
            href = a_tag.get('href')
            title = a_tag.text
    
            date = parse_date(meta[i].find('span').text)

            obj = {'source': "MarketWatch"}
            obj['href'] = href
            obj['title'] = title
            obj['date'] = date[:10]
            
            articles.append(obj)
        
        if num_page % 10 == 0:
            print("MarketWatch" + str(num_page) + " pages done!")


def parse_date(date_string):

    token = date_string.split()

    mm = "00"
    if token[2] == "January":
        mm = "01"
    elif token[2] == "Febuary":
        mm = "02"
    elif token[2] == "March":
        mm = "03"
    elif token[2] == "April":
        mm = "04"
    elif token[2] == "May":
        mm = "05"
    elif token[2] == "June":
        mm = "06"
    elif token[2] == "July":
        mm = "07"
    elif token[2] == "August":
        mm = "08"
    elif token[2] == "September":
        mm = "09"
    elif token[2] == "October":
        mm = "10"
    elif token[2] == "November":
        mm = "11"
    elif token[2] == "December":
        mm = "12"

    dd = token[3][:-1].zfill(2)

    yyyy = token[4]

    return yyyy + "-" + mm + "-" + dd


all_articles = {}

# articles_economist = getEconomist()

# print('---')

# articles_news_bitocin = getNewsBitcoin()

# print('---')

articles_marketwatch = getMarketWatch()

# for a in articles:
#     if a['date'] in all_articles:
#         all_articles[a['date']].append(a)
#     else:
#         all_articles[a['date']] = [a]

# out_file = open("articles.json", "w")
# json.dump([all_articles], out_file)
# out_file.close()

# print(links[0].find_all('a')[0].get('href'))

# {'title': ?, 'date': ?, img: ?, author: ?, 'href': }

