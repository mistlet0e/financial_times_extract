# import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# !!!!!! just to get a dict of archive url and title
driver = webdriver.Chrome(ChromeDriverManager().install())
# get google.co.in
driver.get("https://www.ft.com/cyber-security")

articles = driver.find_element(By.XPATH, '//ul[@class="o-teaser-collection__list js-stream-list"]')

all_li = articles.find_elements(By.TAG_NAME,"li")
heading_url_pair = {}
final = {}
for li in all_li:
    try:
        heading =  li.find_element(By.XPATH, './/a[contains(@class, "js-teaser-heading-link")]')
        heading_text = heading.text
        url = heading.get_attribute('href')
        heading_url_pair[heading_text] = url
    except:
        pass
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")

for keys in heading_url_pair:
    driver.get('https://archive.ph/')
    driver.find_element(By.XPATH,'//*[@id="q"]').send_keys(heading_url_pair[keys])
    driver.find_element(By.XPATH,'//*[@id="search"]/div[3]/input').click()
    try:
        element = WebDriverWait(driver, 35).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'" +keys+ "')]"))
        )
        new_url = driver.find_element(By.XPATH,"//a[contains(text(),'" +keys+ "')]").get_attribute('href')
        final[keys] = new_url
    finally:
        pass