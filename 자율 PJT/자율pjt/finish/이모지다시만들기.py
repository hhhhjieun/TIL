import pandas as pd

# 엑셀 파일 불러오기
file1 = pd.read_excel('emoji_re.xlsx') 
file2 = pd.read_excel('movie_info2.xlsx')  

titles = file1['영화 제목'].unique()

filtered_data = file2[file2['영화 제목'].isin(titles)]

filtered_data.to_excel('filtered_movies.xlsx', index=False)
