# Python program to demonstrate
# selenium
 
# import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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
driver.get("https://twitter.com/i/flow/login")

# login and also input the username if there is additional verification
driver.implicitly_wait(5)
driver.find_element_by_xpath('//input[@autocomplete="username"]').send_keys('emillau@hkex.com.hk')

driver.find_element_by_xpath("//div[@role='button'][contains(.,'Next')]").click()
driver.implicitly_wait(3)

if hasxpath('//*[contains(text(),"Enter your phone number or username")]') == True:
    print("testing")
    driver.find_element_by_xpath('//input[@autocomplete="on"]').send_keys('Emil81542420022')
    driver.find_element_by_xpath("//div[@role='button'][contains(.,'Next')]").click()

driver.find_element_by_xpath('//input[@autocomplete="current-password"]').send_keys('P@ssw0rd123!')
driver.implicitly_wait(1)
driver.find_element_by_xpath("//div[@role='button'][contains(.,'Log in')]").click()

#logged in
#searching latest hkex post in twitter
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[contains(@href,'explore')]").click()
driver.find_element_by_xpath('//input[@placeholder="Search Twitter"]').send_keys('HKEX'+ "\n")
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a').click()
#"//a[contains(text(),'Latest')]"

#scroll and extract post text
scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    tweets = driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')

    for tweet in tweets:
            # ...
        tweet_text = tweet.find_element(By.CSS_SELECTOR,'div[data-testid="tweetText"]').text
        print(tweet_text)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break
