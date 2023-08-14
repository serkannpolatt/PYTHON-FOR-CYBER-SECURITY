# Import necessary libraries / Gerekli kütüphaneleri içe aktar
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

# Create a set to keep track of visited URLs / Ziyaret edilen URL'leri takip etmek için bir küme oluştur
visited_urls = set()

# Define a function to crawl URLs and search for a keyword / URL'leri tarama ve belirli bir anahtar kelimeyi arama işlevini tanımla
def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    # Check if the request was successful (status code 200) / İstek başarılı mı kontrol et (durum kodu 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)

        # Loop through the URLs found on the page / Sayfadaki bulunan URL'leri döngüyle geziyoruz
        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                url_join = urljoin(url, urls2)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join, keyword)
            else:
                pass

# Get user input for URL and keyword / Kullanıcıdan URL ve anahtar kelime girişi al
url = input("Enter the URL you want to scrape: ")
keyword = input("Enter the keyword to search for in the provided URL: ")

# Start crawling and searching for the keyword / Taramayı başlat ve anahtar kelimeyi ara
spider_urls(url, keyword)
