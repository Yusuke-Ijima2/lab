import requests
from bs4 import BeautifulSoup

# ヤフーニュースのトップページ情報を取得する
URL = "https://news.yahoo.co.jp/topics"
rest = requests.get(URL)

# BeautifulSoupにヤフーニュースのページ内容を読み込ませる
soup = BeautifulSoup(rest.text, "html.parser")

# ヤフーニュースの見出しとURLの情報を取得して出力する
topics_field = soup.find_all('p', class_='sc-dqBHgY fTaokj') # ①
topics_contents = soup.find_all('a', class_='sc-btzYZH kitJFB') # ②

news_fields = []
news_contents = []
for field in topics_field:
    news_fields.append(field.get_text())

for content in topics_contents:
    news_contents.append(content.get_text())

# n = 8
# for i in range(0, len(news_contents), n):
#     news_contents.append(news_contents[i:i+n])
#     # print(news_contents)

# print(news_fields)
# print(news_contents)
# print(len(news_contents))