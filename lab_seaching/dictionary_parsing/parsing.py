from janome.tokenizer import Tokenizer
from wordcloud import WordCloud

import collections

with open('lab_seaching/q_sentiment_test.txt', 'r') as f:
    parsing_list = f.read().split("\n")
    # print(parsing_list)

t = Tokenizer()
results = []    
for parsing in parsing_list:
    # 名詞、動詞、形容詞を切り替えて使う
    result = [token.base_form for token in t.tokenize(parsing) if token.part_of_speech.split(',')[0] in ['形容詞']]
    results.extend(result)

# 単語の頻度を確認
c = collections.Counter(results)
print(c.most_common())
print(results)

# 削除するワードをリスト化
stopwords = ['ん', 'よう', 'の', 'こと', 'さ', 'そう', 'まま', 'はず']

# wordcloud
#日本語のフォントパス
fpath = '/Library/Fonts//Arial Unicode.ttf'
text = ' '.join(results) # 区切り文字を「・」にして文字列に変換
print(text)
# 単語の最大表示数は500に設定
wordcloud = WordCloud(background_color='white', font_path=fpath, width=800, height=600, max_words=500, stopwords=set(stopwords)).generate(text)
print(wordcloud)
wordcloud.to_file('./wordcloud.png')