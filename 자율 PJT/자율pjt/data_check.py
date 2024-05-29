import pandas as pd


# 1번 엑셀 파일 로드
df1 = pd.read_excel('movie_info.xlsx')
# 2번 엑셀 파일 로드
df2 = pd.read_excel('movie_emoji_final.xlsx')

# 1번 파일에서 제목 열 중복 제거
unique_titles_df1 = df1['영화 제목']

# 2번 파일에서 제목 열만 추출
titles_df2 = df2['제목'].drop_duplicates()

# 공통되지 않는 제목 찾기
non_overlapping_df2 = df2[~df2['제목'].isin(unique_titles_df1)]



print("1번 파일에서 중복 제거된 제목 중 2번 파일에 없는 제목들:")
print(non_overlapping_df2)

# non_overlapping_df2.to_excel('data_check_movie_quote.xlsx', index=False)