from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import json

# 1. Selenium'un Webdriver sınıfını kullanarak bir adet options adında ChromeOptions tanımlayınız.
options = Options()

# 2. Tanımladığınız options’a tam ekran özelliği ekleyiniz.
options.add_argument("--start-fullscreen")

# 3. Bir önceki adımlarda hazırladığınız options’ı da kullanarak bir adet driver adında Chrome tarayıcısı oluşturunuz.
driver = webdriver.Chrome(options=options)

# Wikipedia ana sayfası URL'si
url = 'https://en.wikipedia.org/wiki/Main_Page'

# 4. Ana Sayfayı driver ile açınız ve inceleyiniz.
driver.get(url)
time.sleep(3)

# 5. Örneğin, ana sayfadaki başlıkları (h1) ve yayınlanma tarihlerini kazıyacak XPath sorgularını yazınız.
article_xpath = "//div[@id='mp-itn']//ul/li/a"
date_xpath = "//div[@id='mp-itn']//ul/li/span[@class='mw-headline']"

def scrape_wikipedia_articles(driver):
    # Makale başlıklarını ve tarihlerini depolamak için boş listeler oluşturun
    articles = []
    
    # XPath kullanarak makale başlıklarını bulun
    article_elements = driver.find_elements(By.XPATH, article_xpath)
    date_elements = driver.find_elements(By.XPATH, date_xpath)
    
    # Başlıkları ve tarihleri tek tek alın
    for article_elem, date_elem in zip(article_elements, date_elements):
        title = article_elem.get_attribute('title')
        date = date_elem.text
        
        # Verileri bir sözlüğe ekleyin
        article_data = {
            'title': title,
            'date': date
        }
        
        # Sözlüğü listeye ekleyin
        articles.append(article_data)
    
    return articles

# Wikipedia ana sayfasındaki makaleleri kazıyın
wikipedia_articles = scrape_wikipedia_articles(driver)

# Sonuçları JSON dosyasına kaydedin
with open('wikipedia_articles.json', 'w', encoding='utf-8') as f:
    json.dump(wikipedia_articles, f, ensure_ascii=False, indent=4)

# Tarayıcıyı kapat
driver.quit()
