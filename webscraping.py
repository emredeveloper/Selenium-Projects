import requests
from bs4 import BeautifulSoup
import pandas as pd

# Ana URL ve kategori URL'si
base_url = 'https://books.toscrape.com/'
category_url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'

# Kullanıcı aracısı (User-Agent) başlığı ile istek gönderme
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# İstek gönderme ve içeriği alma
response = requests.get(category_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Ürün listesini bulma
products = soup.find_all('article', class_='product_pod')

# Veri saklamak için boş listeler oluşturma
titles = []
prices = []
taxes = []

# Her ürün için bilgileri çıkarma
for product in products:
    title = product.h3.a.get_text()
    price = product.find('p', class_='price_color').get_text()
    avability = product.find('p', class_='price_color').find_next_sibling('p').get_text()  # Tax bilgisi
    
    titles.append(title)
    prices.append(price)
    taxes.append(avability)

# DataFrame oluşturma
data = {
    'Title': titles,
    'Price': prices,
    'avability': taxes  # Tax bilgisi olarak alınacak
}
df = pd.DataFrame(data)

# CSV dosyasına yazma
df.to_csv('travel_books.csv', index=False)

print('Travel kategorisindeki kitaplar başarıyla travel_books.csv dosyasına kaydedildi.')
