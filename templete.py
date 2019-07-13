import pandas as pd
import numpy as np

def appleCrawler(url):
    #impletement here
    return content

def chinaCrawler(url):
    #impletement here
    return content

def ltnCrawler(url):
    #impletement here
    return content

def udnCrawler(url):
    #impletement here
    return content

def if __name__ == "__main__":
    df = pd.read_csv('dataset/NC_1.csv')
    df['content'] = ''
    df = df.set_index('News_Index')
    all_news = []
    for index, row in df.iterrows():
        if 'chinatimes' in row.News_URL:
            content = chinaCrawler(row.News_URL)
            all_news.append(contnet)
        elif 'appledaily' in row.News_URL:
            content = appleCrawler(row.News_URL)
            all_news.append(contnet)
        elif 'ltn' in row.News_URL:
            contnet = ltnCrawler(row.News_URL)
            all_news.append(content)
        elif 'udn' in row.News_URL:
            contnet = udnCrawler(row.News_URL)
            all_news.append(content)
        else:
            miss_news = row.News_URL
            print(miss_news + 'missed')
            all_news.append('miss')
    df['content'] = pd.Series(all_news)
    df.to_csv('NC_1_crawed.csv')

