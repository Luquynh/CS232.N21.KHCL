
from selenium import webdriver
from selenium.webdriver.common.by import By
from time  import sleep
import pandas as pd

import os

#1 Khai bao bien browser
browser=webdriver.Chrome(executable_path="./chromedriver.exe")

# #2. Mo thu 1 trang web
browser.get("https://scholar.google.com/citations?hl=vi&user=I8bNZakAAAAJ")
sleep(5)

showmore_paper = browser.find_element(By.ID, 'gsc_bpf_more')
showmore_paper.click()
sleep(5)

title_paper=[]
author_paper=[]
year_paper=[]

paper_list = browser.find_elements(By.CLASS_NAME,'gsc_a_tr')
print('Tong paper:',len(paper_list))
num_paper = 1
for paper in paper_list:
    print(num_paper)
    num_paper += 1
    title = paper.find_element(By.CLASS_NAME,'gsc_a_at')
    authors = paper.find_element(By.CLASS_NAME,'gs_gray')
    year=paper.find_element(By.CLASS_NAME,'gsc_a_y')

    title_paper.append(title.text)
    author_paper.append(authors.text)
    year_paper.append(year.text)

data={'Title': title_paper,'Authors':author_paper,'Year':year_paper}

pd.DataFrame(data).to_csv('C:\\Users\\thuan\\Downloads\\CS232.M21.KHCL-main\\CS232.M21.KHCL-main\\Lab\\paper.csv')

browser.close()
