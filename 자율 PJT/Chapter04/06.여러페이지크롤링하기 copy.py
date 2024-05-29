import requests
from bs4 import BeautifulSoup
import time
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요")
lastpage = int(pyautogui.prompt("몇 페이지까지 크롤링?"))

page_num = 1
for i in range(1, lastpage*10, 10):
    response = requests.get(f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}&start={lastpage}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.select("div.info_group") # 뉴스 기사 div 10개 추출
    for article in articles:
        links = article.select("a.info") # 리스트
        if len(links) >= 2: # 링크가 2개 이상이면
            url = links[1].attrs['href'] # 두번째 링크의 href를 추출
            print(url)
            response = requests.get(url, headers={'User-agent': 'Mozila/5.0'})
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 만약 연예 뉴스라면
            if 'entertain' in response.url:
                title = soup.select_one(".end_tit")
                content = soup.select_one("#articeBody")
            elif 'sports' in response.url:
                title = soup.select_one("h2.NewsEndMain_article_title__kqEzS")
                content = soup.select_one("#comp_news_article")
                # 본문 내용안에 불필요한 div 삭제
                divs = content.select("div")
                for div in divs:
                    div.decompose()
                paragraphs = content.select("p")
                for p in paragraphs:
                    p.decompose()
                    
            else:
                # title = soup.select_one("#articleTitle")
                content = soup.select_one("article")
            print("==========링크==========\n", url)
            # print("==========제목==========\n", title.text.strip())
            print("==========본문==========\n", content.text.strip())
            time.sleep(0.3) # 시간 걸어주기
    
    page_num += 1