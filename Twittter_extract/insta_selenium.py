# Python program to demonstrate
# selenium
 
# import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# create webdriver object
driver = webdriver.Chrome(ChromeDriverManager().install())
# get google.co.in
driver.get("https://www.instagram.com/accounts/login/")


def hasxpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False
    

#pw
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('emil_flower_shop')

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('1Loveadidas!$')
if hasxpath('//*[@id="loginForm"]/div/div[4]/button/div') == True:
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[4]/button/div').click()
else:
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()

driver.implicitly_wait(10)

notNowButton = WebDriverWait(driver, 15).until(
    lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')
)
notNowButton .click()

