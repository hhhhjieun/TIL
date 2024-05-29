# -*- coding: utf-8 -*-
import openai
import os
import pandas as pd
import time

# 1. 엑셀 파일 로드
input_excel_path = "./movie_info.xlsx" 
data = pd.read_excel(input_excel_path)

data = data[700:len(data)]

# '제목'과 '줄거리' 열 추출
titles = data['영화 제목']
summaries = data['영화 줄거리']
actors = data['영화 배우']

# 이모지를 저장할 리스트
word_results = []

for title, summary, actor in zip(titles, summaries, actors):
    prompt = f"영화 제목과 줄거리, 영화 배우를 바탕으로 관련 단어 30개를 만들어줘. 근데 제목이랑 줄거리가 영화배우보다 더 분량이 많아야해. 제목 : {title}, 줄거리 : {summary}, 영화 배우: {actor}"

    completion = openai.chat.completions.create(
    model="gpt-4",
    # model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
        ]
    )

    response_text = completion.choices[0].message.content

    # print(response_text)
    word_lines = response_text.split('\n')

    for word in word_lines:
        try:
            word_content = word.split('.')[1].strip()
            print(word_content)
            word_results.append((title, word_content))
        except:
            word_results.append((title, word))

    time.sleep(10)


# 결과를 엑셀에 저장
output_df = pd.DataFrame(word_results, columns=['제목', '단어'])
output_df.to_excel('movie_word_list8.xlsx', index=False)


