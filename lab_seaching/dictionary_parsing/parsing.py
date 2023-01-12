from janome.tokenizer import Tokenizer
from wordcloud import WordCloud

with open('lab_seaching/q_sentiment_test.txt', 'r') as f:
    parsing_list = f.read().split("\n")
    # print(parsing_list)

t = Tokenizer()
results = []
for parsing in parsing_list:
    # 全角スペースを削除 # リストに追加
    tokens = list(t.tokenize(parsing, wakati=True))
    result = [i.replace('\u3000','') for i in tokens] 
    results.extend(result)

print(results)

# wordcloud
#日本語のフォントパス
fpath = '/Library/Fonts//Arial Unicode.ttf'
text = ' '.join(results) # 区切り文字を「・」にして文字列に変換
print(text)
# 単語の最大表示数は500に設定
wordcloud = WordCloud(background_color='white', font_path=fpath, width=800, height=600, max_words=500).generate(text)
print(wordcloud)
wordcloud.to_file('./wordcloud.png')