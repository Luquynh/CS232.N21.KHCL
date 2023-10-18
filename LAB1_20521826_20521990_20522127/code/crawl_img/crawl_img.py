from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib.request 
from time import sleep
from selenium.webdriver.common.by import By



def initDriver():
    options = Options()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options)  
    return browser

browser = initDriver()

# Access to google image in the browser
browser.get('https://images.google.com/')
# '//*[@id="REsRA"]'
# Find search input 
sleep(3)
search_input = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')

# Type information which we want to search
info = 'dog'
search_input.send_keys(info)

# Then press key enter to search
search_input.send_keys(Keys.ENTER) 

src_images = []
path = 'D:\\ttdpt\\lab1\\image_search\\image_search'


for i in range(1, 11):
    try:
        img = browser.find_element(by=By.XPATH, value = '//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')
        src_images.append(img.get_attribute("src"))
        
        number = 0
        for src in src_images:
            urllib.request.urlretrieve(src, path + str(number) + ".jpg")
            number += 1
            print('thanh cong')
    except:
        continue


sleep(120)
browser.close()
