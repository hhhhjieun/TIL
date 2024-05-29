import pandas as pd

# 영화정보 가져오기
df1 = pd.read_excel('./영화최종.xlsx')

# 영화명대사 가져오기 
df2 = pd.read_excel('./영화명대사최최종.xlsx')

# 영화제목을 기준으로 inner 조인
merged_df = pd.merge(df1, df2, on='영화 제목', how='inner')

# 중복제거해서 리스트 만들기
titles = merged_df['영화 제목'].drop_duplicates().tolist()

# 영화정보랑 비교하기
result_df = df2[df2['영화 제목'].isin(titles)]

result_df.to_excel('영화명대사최최최종.xlsx', index=False)
