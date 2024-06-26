import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random

# Başlık bilgilerini eklemek ve tarayıcıyı başlatmak için seçenekler
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument('--headless')  # Tarayıcıyı arka planda çalıştırmak için
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# WebDriver kurulumu (manuel yol ile)
chrome_driver_path = "C:\chromedriver\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

# Amazon'a gitme
driver.get("https://www.amazon.com")

# Rastgele gecikme eklemek
time.sleep(random.uniform(2, 5))

# Arama kutusunu bulma
search_box = driver.find_element(By.ID, "twotabsearchtextbox")

# Aranacak ürünü girme
product_name = "laptop"
search_box.send_keys(product_name)
search_box.send_keys(Keys.RETURN)

# Sayfanın yüklenmesini bekleme
time.sleep(random.uniform(2, 5))

# Ürün bilgilerini toplayacak liste
products_info = []

# Ürün bilgilerini çekme
product_elements = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
for product_element in product_elements:
    try:
        product_name_element = product_element.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
        product_name = product_name_element.text

        product_price_element = product_element.find_element(By.XPATH, ".//span[@class='a-price-whole']")
        product_price = product_price_element.text

        products_info.append((product_name, product_price))
    except Exception as e:
        print(f"Error: {e}")
        continue

# Tarayıcıyı kapatma
driver.quit()

# CSV dosyasına yazma
csv_file = "amazon_laptop_prices.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Laptop Adı", "Fiyat"])
    writer.writerows(products_info)

print(f"Fiyatlar {csv_file} dosyasına kaydedildi.")
