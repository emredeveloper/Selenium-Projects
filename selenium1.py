import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://miuul.com/katalog")
time.sleep(5)
print(driver.title)
elemenet = driver.find_elements(By.XPATH,"//a[@id='login']")
btn = elemenet[0]

aramalar = driver.find_elements(By.XPATH,"//input[@name = 'arama']")
arama = aramalar[0]
#arama.send_keys("Data Science",Keys.ENTER)
#btn.click()
#time.sleep(5)


input_ileri = driver.find_elements(By.XPATH,"/html/body/div[3]/main/div[2]/div/div[1]/form/div[2]/div[3]/input")
input_orta = driver.find_elements(By.XPATH,"/html/body/div[3]/main/div[2]/div/div[1]/form/div[2]/div[2]/input") 
#input_ileri[0].click() if input else None  
input_orta[0].click() if input else None  
time.sleep(5)

course_block = driver.find_elements(By.XPATH,"/html/body/div[3]/main/div[2]/div/div[2]/div[3]")
liste = []
if input_orta:
    print(liste.append(course_block))
    
