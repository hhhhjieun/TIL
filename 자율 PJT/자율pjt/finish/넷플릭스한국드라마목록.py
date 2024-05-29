from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
# from tqdm import tqdm
import time
import re

excel = './drama_links.xlsx'

df = pd.read_excel(excel)

drama_set = []

for i in range(len(df)):
    url = df['링크'][i]

    # 웹 드라이버 설정 및 URL 접속
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
    driver.get(url)

    # 페이지가 완전히 로드될 때까지 잠시 대기
    time.sleep(2)

    # 현재 페이지의 HTML을 가져옴
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 드라마 제목 추출
    drama_title_element = soup.select_one("h1.HswM2oQL span") 

    drama_title = drama_title_element.text  # 텍스트 추출

    # 드라마 포스터 추출  
    drama_item = soup.select_one("div > div > span > span > img.W0Vl59Hf")
    drama_img_src = drama_item.get('src')
    drama_image = drama_img_src

   # 드라마 시놉시스 추출
    drama_outline_elements = soup.select("blockquote")  # 모든 blockquote 요소 선택
    drama_outlines = []  # 시놉시스 저장을 위한 리스트
    
    # 각 blockquote에서 div 텍스트 추출
    for outline in drama_outline_elements:
        div_element = outline.select_one("div.raQitNmp")  # div 요소 선택
        if div_element:
            # print(div_element.text)
            drama_outlines.append(div_element.text)
    

    if drama_outlines:
        drama_outlines_str = ' '.join(drama_outlines)
    
    drama_set.append([drama_title, drama_outlines_str, drama_image])


data = pd.DataFrame(drama_set, columns=['드라마 제목', '드라마 줄거리', '드라마 포스터'])

data.to_excel('./drama_list.xlsx', index=False)