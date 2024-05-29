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
url = "https://namu.wiki/w/%EB%84%B7%ED%94%8C%EB%A6%AD%EC%8A%A4%20%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90%20%ED%95%9C%EA%B5%AD%20%EB%93%9C%EB%9D%BC%EB%A7%88?from=%EB%84%B7%ED%94%8C%EB%A6%AD%EC%8A%A4%20%ED%95%9C%EA%B5%AD%20%EB%93%9C%EB%9D%BC%EB%A7%88"

# 웹드라이버 설정 및 URL 접속
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

dramas = driver.find_elements(By.CSS_SELECTOR, 'td._ba832eed82a14e6b3bc9304cd9b2a6d0 > div > a')

drama_links = []

for i in range(11, len(dramas)):
    links_list = []
    links = dramas[i].get_attribute('href')
    drama_links.append(links)

driver.close() # 브라우저 닫기

# DataFrame 생성 및 Excel 파일로 저장
data = pd.DataFrame(drama_links, columns=['링크'])
data.to_excel('./drama_links.xlsx', index=False)
