import requests
from bs4 import BeautifulSoup
import os

# Ana URL ve Makine Öğrenimi kategorisi URL'si
base_url = 'https://www.tutorialspoint.com'
ml_category_url = 'https://www.tutorialspoint.com/machine_learning_tutorials.htm'

# Kullanıcı aracısı (User-Agent) başlığı ile istek gönderme
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Makine Öğrenimi kategorisi sayfasını alma
response = requests.get(ml_category_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Makale bağlantılarını bulma
article_links = soup.find_all('a', class_='toc-chapter')

# Veri saklamak için boş listeler oluşturma
articles = []

# Her makale için bilgileri çıkarma
for link in article_links:
    article_url = base_url + link.get('href')
    article_response = requests.get(article_url, headers=headers)
    article_soup = BeautifulSoup(article_response.content, 'html.parser')
    
    # Makale başlığını ve içeriğini bulma
    title = article_soup.find('h1').get_text()
    content_div = article_soup.find('div', class_='mui-col-md-6')
    content = content_div.get_text(separator='\n') if content_div else ''
    
    articles.append((title, content))

# Txt dosyasına yazma
if not os.path.exists('ml_articles'):
    os.makedirs('ml_articles')

for i, (title, content) in enumerate(articles):
    with open(f'ml_articles/article_{i+1}.txt', 'w', encoding='utf-8') as file:
        file.write(f"Title: {title}\n\n{content}")

print('Makine Öğrenimi kategorisindeki makaleler başarıyla txt dosyalarına kaydedildi.')
