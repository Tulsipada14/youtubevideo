from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import RawConfigParser
from selenium.webdriver.common.keys import Keys
import time
#only heroku
import os
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

url = 'https://www.youtube.com/watch?v=9Zj47LygqGk&list=PLcQdgZtzWOA2_V8KVyr9TPppRrUQnFWS6'

#only heroku
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)




def Playvideo():
    print('Opening Link in chrome..........')

    #onliy offline
#     driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    driver.get('https://www.youtube.com/c/DrAndroidGuruji/playlists')
    driver.find_element(By.XPATH, "//*[@title='Android Gurujis All video :-Android application']").click()
    print('click by playlists')
    driver.maximize_window()
    
    while True:
        time.sleep(60)
        el = driver.find_element(By.XPATH,"//*[@id='container']/h1/yt-formatted-string")
        #FOR PUBLIC IP
        from requests import get
        ip = get('https://api.ipify.org').text
        print ('My public IP address is:', ip)
        if el.text == 'Emoji':
            driver.close()
            Playvideo()
        print(el.text)
    # time.sleep(86400)
    driver.close()
    

if __name__ == '__main__':
    Playvideo()
