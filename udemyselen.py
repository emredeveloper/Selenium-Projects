from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
def scrape_website():
    driver = webdriver.Chrome()
    driver.get("https://atilsamancioglu.com/")
    driver.maximize_window()

    driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div[3]/nav/div/ul/li[3]/a').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/main/article[1]/div/p[2]/a').click()
    time.sleep(5)

    metin = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/main/article/div/p[2]').text
    driver.quit()

    return metin


class TestScrapeWebsite(unittest.TestCase):
    def test_scrape_website(self):
        metin = scrape_website()
        self.assertIsInstance(metin, str)
        self.assertGreater(len(metin), 0, "Scraped text should not be empty")

if __name__ == "__main__":
    unittest.main()