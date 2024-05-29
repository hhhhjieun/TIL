import pandas as pd

# 엑셀 파일 불러오기
input_excel_path = "./emoji_movie_plus.xlsx" 
df = pd.read_excel(input_excel_path)  # 'yourfile.xlsx'는 실제 파일 경로로 대체해야 합니다.

# 특정 텍스트(♂, ♀) 제거하고 새 열 '이모지'에 저장
df['뉴이모지'] = df['이모지'].replace({'♂': '', '♀': ''}, regex=True)

df['뉴이모지'] = df['뉴이모지'].apply(lambda x: x.replace(' ', '') if isinstance(x, str) else x)
# 결과를 새로운 엑셀 파일로 저장
df.to_excel('emoji_movie_plus_modify1.xlsx', index=False)
