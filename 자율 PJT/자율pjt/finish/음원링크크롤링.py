import pandas as pd

excel_path = './drama_info_crawling_final.xlsx'
data = pd.read_excel(excel_path)

titles = data['드라마 제목']

for title in titles:
    