# import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# def initilaize_driver():
#     options = webdriver.ChromeOptions()
#     header = Headers().generate()['User-Agent']
#     options.add_argument('--headless')  # runs browser in headless mode
#     options.add_argument('--no-sandbox')
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--disable-gpu')
#     options.add_argument('--log-level=3')
#     options.add_argument('--disable-notifications')
#     options.add_argument('--disable-popup-blocking')
#     options.add_argument('--user-agent={}'.format(header))
   
#     drive =webdriver.Chrome(executable_path=ChromeDriverManager().install(),
#                         options= options, )
#     drive = webdriver.Chrome(r'C:\selinum\chromedriver.exe')
#     return drive

def hasxpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False
# create webdriver object
driver = webdriver.Chrome(ChromeDriverManager().install())
# get google.co.in
driver.get("https://www.ft.com/cyber-security")
df = pd.read_csv('Twittter_extract\data_financial_times.csv')  
heading_url_pair = []


#articles = driver.find_elements(By.XPATH, './/li[contains(@class, "o-teaser-collection__item o-grid-row")]')
articles = driver.find_element_by_xpath('//ul[@class="o-teaser-collection__list js-stream-list"]')

all_li = articles.find_elements_by_tag_name("li")
for li in all_li:
    try:
        heading =  li.find_element_by_xpath('.//a[contains(@class, "js-teaser-heading-link")]')
        heading_text = heading.text
        url = heading.get_attribute('href')
        if heading not in df.values:
            heading_url_pair.append([heading_text,url])
            # print(heading_text)
            # df2 = pd.DataFrame([[heading_text,url]], columns=df.columns)
            # df = pd.concat([df, df2], ignore_index = True)
            # print(df)
    except:
        pass
#heading to archive tab to generate 
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")
for index, pair in enumerate(heading_url_pair):
    driver.get('https://archive.ph/')
    driver.find_element_by_xpath('//*[@id="q"]').send_keys(pair[1])
    driver.find_element_by_xpath('//*[@id="search"]/div[3]/input').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//a[contains(text(),'" +pair[0]+ "')]").click()
    try:
        element = WebDriverWait(driver, 35).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-component="article-body"]'))
        )
        paragraphs = driver.find_element_by_xpath('//div[@data-component="article-body"]')
        print(paragraphs.text)
    finally:
        pass
    

# for article in articles:
#     heading =  driver.find_element_by_xpath('//a[contains(@class, "js-teaser-heading-link")]')
#     heading_text = heading.text
#     url = heading.get_attribute('href')
#     print(heading_text,url)