from bs4 import BeautifulSoup 
import bs4
import requests
import regex
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url',dest='url',help='Enter url with product reviews to get the associated reviews.')
    options = parser.parse_args()
    return options

def get_soup(url):
       headers = {
       'authority': 'www.amazon.com',
       'pragma': 'no-cache',
       'cache-control': 'no-cache',
       'dnt': '1', #set to one to not track
       'upgrade-insecure-requests': '1',
       'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'sec-fetch-site': 'none',
       'sec-fetch-mode': 'navigate',
       'sec-fetch-dest': 'document',
       'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
       }
       res = requests.get(url, headers = headers)
       soup = BeautifulSoup(res.text.encode('cp1252', errors='replace'), 'html.parser')
       return soup
       
def get_reviews(soup):
       reviews =  str(soup.find_all('span', attrs={'class':'a-size-base review-text review-text-content'}))
       #print(reviews)
       reviews2 = regex.findall('<span>\n (.*)\n</span>', reviews)
       while reviews2:
        amrevs = open('amazon_reviews.txt', 'a')
        amrevs.write(str(reviews2))
        amrevs.write('\n')
        amrevs.close()
        print(reviews2)
        break
#get_reviews("https://www.amazon.com/Retrospec-Solana-Thick-Nylon-Strap/product-reviews/B091FX694F/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews")

opt = get_args()
ampage = str(opt.url)+"&pageNumber="

for i in range(1, 999): 
    soup = get_soup(ampage+str(i))
    get_reviews(soup)
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break