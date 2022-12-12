import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

total_page=35
# page_size=25
page_size=100
base_url = 'https://www.airlinequality.com/airline-reviews/british-airways'

list_df = []

for i in range(1, total_page+1):
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"
    
    r = requests.get(url)
    content = r.content
    parsed_content = bs(content, 'lxml')
    
    articles = parsed_content.find_all('article', attrs={'itemprop': 'review'})
    for article in articles:
        data = {}
        review_rating = {}
        
        try:
            _id = article.find("div", attrs={"class": "body"})['id']
        except Exception as e:
            _id = ''
        
        try:
            review = article.find("div", attrs={"class": "text_content"}).get_text(' ', strip=True)
        except Exception as e:
            review = ''
        
        try:
            rating = article.find("div", attrs={"itemprop": "reviewRating"}).get_text('', strip=True)
        except Exception as e:
            rating = ''
        
        try:
            header = article.find("div", attrs={"class": "body"}).find('h2', attrs={"class": "text_header"}).get_text('', strip=True)
        except Exception as e:
            header = ''
        
        try:
            sub_header = article.find("div", attrs={"class": "body"}).find('h3', attrs={"class": "text_sub_header"}).get_text(' ', strip=True)
        except Exception as e:
            sub_header = ''
        
        try:
            author = article.find("div", attrs={"class": "body"}).find('h3', attrs={"class": "text_sub_header"}).find('span', attrs={"itemprop": "author"}).get_text('', strip=True)
        except Exception as e:
            author =  ''
        
        try:
            time_published = article.find("div", attrs={"class": "body"}).find('h3', attrs={"class": "text_sub_header"}).find('time', attrs={"itemprop": "datePublished"}).get_text('', strip=True)
        except Exception as e:
            time_published =  ''      
       
       
        data = {
            'id': _id,
            'review':review,
            'rating' :rating, 
            'header' :header,
            'sub_header' :sub_header,
            'author' :author,
            'time_published' :time_published
        }
        
        rows = article.find('table', attrs={'class': 'review-ratings'}).find_all('tr')
        for row in rows:
            td = row.find_all('td')
            try:
                head = td[0].get_text(strip=True)   
            except Exception as e: 
                head = ''
                
            try:
                vals = td[-1].select('span.star.fill')
                val = vals[-1].get_text(strip=True)
            except Exception as e:
                try:
                    val = td[-1].get_text(strip=True)     
                except Exception as e:
                    val = ''
                 
            review_rating[head] = val
    
        data.update(review_rating)
        list_df.append(data)
    
    print(f'Sleep! (1 sec), scrapped {i} pages')
    time.sleep(1)
    

    # dict to dataframe
    df = pd.DataFrame.from_dict(list_df)
    df.to_csv(f'dataframe_totpage_{i}.csv', index=False, sep=';')
    # break