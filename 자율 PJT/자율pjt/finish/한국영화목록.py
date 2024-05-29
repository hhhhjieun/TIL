from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
# from tqdm import tqdm
import time
import re

# url 설정
url = "https://namu.wiki/w/%ED%95%9C%EA%B5%AD%20%EC%98%81%ED%99%94/%EB%AA%A9%EB%A1%9D"

# 웹드라이버 설정 및 URL 접속
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

movies = soup.select('div.BFgp7eXo')
title_list = []

for movie in movies:
    titles = movie.select('a.b8VqAR6G')
    for title in titles: 
        title_list.append(title.text)

# DataFrame 생성 및 Excel 파일로 저장
data = pd.DataFrame(title_list, columns=['제목'])
data.to_excel('./movies.xlsx', index=False)

driver.close() # 브라우저 닫기

