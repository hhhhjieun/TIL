import pandas as pd

df1 = pd.read_excel('./movie_thumb_crawling.xlsx')
df2 = pd.read_excel('./movie_quote_crawling_진희.xlsx')

appended_df = pd.concat([df1, df2], ignore_index=True)

# result_df = appended_df.drop_duplicates(subset=['영화 제목'])

# 결과를 새로운 엑셀 파일로 저장
appended_df.to_excel('영화명대사최종.xlsx', index=False)