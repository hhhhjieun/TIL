# -*- coding: utf-8 -*-
import openai
import os
import pandas as pd
import time


# 1. 엑셀 파일 로드
input_excel_path = "./data_check_movie.xlsx" 
data = pd.read_excel(input_excel_path)

# data = data[700:len(data)]

# '제목'과 '줄거리' 열 추출
titles = data['영화 제목']
summaries = data['영화 줄거리']

# 이모지를 저장할 리스트
emoji_results = []

for title, summary in zip(titles, summaries):
    prompt = f"영화 줄거리를 바탕으로 이모지를 만들어서 맞추는 게임을 하기위한 이모지를 만들거야. 영화 {title}의 줄거리인 {summary}를 바탕으로 5가지, 총 10가지를 만들어주는데 각각 이모지 5개로, 총 10가지 만들어줘. 이모지에대한 설명은 필요없어. 제발 부탁할게!! 제목과 줄거리에 부합하는 이모지로 만들어주고 많지도 적지도 않게 각각의 문제가 이모지 딱 5개로 10가지의 문제를 만들어줘."

    completion = openai.chat.completions.create(
    model="gpt-4",
    # model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
        ]
    )

    response_text = completion.choices[0].message.content

    # print(response_text)
    emoji_lines = [
        line for line in response_text.split('\n')  # 응답을 줄로 분할
        if line.strip().startswith(tuple(str(i) for i in range(1, 11)))  # 1~10으로 시작하는 줄 추출
    ]

    for emoji_line in emoji_lines:
        try:
            emoji_content = ' '.join(emoji_line.split('.')[1]).strip()
            print(emoji_content)
            emoji_results.append((title, emoji_content))
        except:
            print(emoji_line)
            emoji_results.append((title, emoji_line))


    time.sleep(10)


# 결과를 엑셀에 저장
output_df = pd.DataFrame(emoji_results, columns=['제목', '이모지'])
output_df.to_excel('emoji_movie_plus.xlsx', index=False)


