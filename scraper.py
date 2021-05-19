import requests
import json
from bs4 import BeautifulSoup
from psaw import PushshiftAPI
import datetime

api = PushshiftAPI()

def getEconomist():

    total_page = 10
    articles = []

    for page in range(1, total_page+1):
        url = "https://www.economist.com/search?q=Bitcoin&page=" + str(page+1)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        contents = soup.find_all('div', class_='css-1ehrfcr e1k9lotg0')

        for content in contents:

            try:
        
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
            
            except Exception as e:
                print(e)
                continue
    
    return articles

def getNewsBitcoin():

    total_page = 1529
    first_page = 15
    articles = []

    for num_page in range(first_page, total_page+1):
        url = "https://news.bitcoin.com/page/" + str(num_page) + "/?s=bitcoin"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        contents = soup.find_all('div', class_='td_module_16 td_module_wrap td-animation-stack')

        for content in contents:

            try:
        
                href = content.find('a').get('href')
                title = content.find('h3', class_="entry-title td-module-title").text
                img = content.find('img').get('src')
                date = content.find('time').get('datetime')

                obj = {'source': "Bitcoin.com"}
                obj['href'] = href
                obj['title'] = title
                obj['img'] = img
                obj['date'] = date
                
                articles.append(obj)

            except Exception as e:
                print(e)
                continue
        
        if num_page % 100 == 0:
            print("news.bitcoin.com " + str(num_page) + " pages done!")
    
    return articles

def getMarketWatch():

    total_page = 357
    articles = []

    for num_page in range(1, total_page+1):
        url = "https://www.marketwatch.com/search?q=bitcoin&Link=MW_SearchAC&mod=keyword_search&mp=806&o=" + str(num_page*15 + 1)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        contents = soup.find_all('div', class_='searchresult')
        meta = soup.find_all('div', class_='deemphasized')

        for i in range(len(contents)):

            try:

                a_tag = contents[i].find('a')
                href = a_tag.get('href')
                title = a_tag.text
        
                date = parse_date(meta[i].find('span').text)

                obj = {'source': "MarketWatch"}
                obj['href'] = href
                obj['title'] = title
                obj['date'] = date
                
                articles.append(obj)

            except Exception as e:
                print(e)
                continue
        
        if num_page % 20 == 0:
            print("MarketWatch" + str(num_page) + " pages done!")
    
    return articles

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

    time = token[0].split(":") 
    hour = time[0]
    minute = time[1]

    if token[1] == "p.m." and hour != "12":
        hour = str(int(hour) + 12)

    hour = hour.zfill(2)

    return yyyy + "-" + mm + "-" + dd + "T" + hour + ":" + minute + ":" + "00Z"

def getReddit():

    posts = []
    start_date = datetime.datetime(2012, 1, 1)
    end_date = datetime.datetime(2021, 4, 1)
    for single_date in daterange(start_date, end_date):

        start_epoch = int(single_date.timestamp())
        end_epoch = int((single_date + datetime.timedelta(days=1)).timestamp())

        submissions = list(api.search_submissions(
            title='bitcoin',
            after=start_epoch,
            before=end_epoch,
            fields=['created_utc','title','subreddit','full_link','score'],
            sort_type='score',
            limit=20))

        for each in submissions:

            obj = {}

            try:
                obj['href'] = each.full_link
                obj['title'] = each.title
                obj['date'] = datetime.datetime.fromtimestamp(each.created_utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                obj['subreddit'] = each.subreddit
                posts.append(obj)
            except:
                continue
        
        print("Reddit on " + single_date.strftime("%Y-%m-%d") + " done")
        
    return posts

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def saveReddit(posts):

    all_posts = {}

    for post in posts:

        date = post['date'][:10]

        if date in all_posts:
            all_posts[date].append(post)
        else:
            all_posts[date] = [post]
    
    out_file = open("posts.json", "w")
    json.dump(all_posts, out_file)
    out_file.close()

def saveArticles(articles):

    all_articles = {}

    for a in articles:

        date = a['date'][:10]

        if date in all_articles:
            all_articles[date].append(a)
        else:
            all_articles[date] = [a]

    out_file = open("articles.json", "w")
    json.dump(all_articles, out_file)
    out_file.close()


if __name__ == "__main__":

    articles = getEconomist()
    articles_news_bitcoin = getNewsBitcoin()
    articles_marketwatch = getMarketWatch()

    print(len(articles_news_bitcoin))
    print(len(articles_marketwatch))

    articles.extend(articles_news_bitcoin)
    articles.extend(articles_marketwatch)

    print(len(articles))

    saveArticles(articles)

    # posts = getReddit()
    # saveReddit(posts)
    