from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import pandas as pd

import os
import argparse


driver = webdriver.Chrome(executable_path="chromedriver.exe")
url = 'https://vnexpress.net/'
driver.get(url)


# Get link of post
list_post = driver.find_elements(By.CSS_SELECTOR,".title-news>a")

list_urls = [post.get_attribute("href") for post in list_post]

print(len(list_urls))

numpost = 1
list_dicts = []

for post in list_urls:
    
    driver.get(post)
    print(numpost)
    numpost += 1
    # Get title
    try:
        title = driver.find_elements(By.XPATH,'//*[@class="title-detail"]')[0].text
    except:
        title = ""

    # Get content
    content = driver.find_elements(By.CSS_SELECTOR,".Normal")
    numcontent = len(content)
    list_content = []
    try:
        for i in range(numcontent):
            content = driver.find_elements(By.XPATH,'//*[@class="Normal"]')[i].text
            list_content.append(content)
    except:
        comment = ""
    


    # Get comment
    cmt = driver.find_elements(By.CSS_SELECTOR,".full_content")
    numcmt = len(cmt)
    list_cmts = []
    try:
        for i in range(numcmt):
            comment = driver.find_elements(By.XPATH,'//*[@class="full_content"]')[i].text
            list_cmts.append(comment)
    except:
        comment = ""
        
    content =""      
    for strs in list_content:
        content += strs
    
    temp_dict = {
        "title": title,
        "content": content,
        "comment": list_cmts
    }
    # print(temp_dict)
    list_dicts.append(temp_dict)


data={'Posts':list_dicts}

pd.DataFrame(data).to_csv('C:\\Users\\thuan\\Downloads\\CS232.M21.KHCL-main\\CS232.M21.KHCL-main\\Lab\\vnexpress.csv')
driver.close()