from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import pandas as pd
import collections

with open('lab_seaching/w_sentiment_file.txt', 'r') as f:
    parsing_list = f.read().split("\n")
    # print(parsing_list)

t = Tokenizer()
results = []    
for parsing in parsing_list:
    # 名詞、動詞、形容詞を切り替えて使う
    result = [token.base_form for token in t.tokenize(parsing) if token.part_of_speech.split(',')[0] in ['名詞']]
    results.extend(result)

# 単語の頻度を確認
c = collections.Counter(results)
# print(c.most_common())
# print(results)

# 削除するワードをリスト化
stopwords = ['ん', 'よう', 'の', 'こと', 'さ', 'そう', 'まま', 'はず']

# wordcloud
#日本語のフォントパス
fpath = '/Library/Fonts//Arial Unicode.ttf'
text = ' '.join(results) # 区切り文字を「 」にして文字列に変換
# print(text)
# 単語の最大表示数は500に設定
wordcloud = WordCloud(background_color='white', font_path=fpath, width=800, height=600, max_words=500, stopwords=set(stopwords)).generate(text)
# print(wordcloud)
wordcloud.to_file('./wordcloud.png')

df_dic = pd.read_csv('pn.csv.m3.120408.trim', sep='\t', names=("名詞", "感情", "動詞句"), encoding='utf-8')
# 辞書の中身と感情の中身を確認
# print(df_dic)
# print(df_dic["感情"].value_counts())
# 感情のうち、p/e/nの項目のみを抽出
df_dic = df_dic[(df_dic["感情"] == 'p') | (df_dic["感情"] == 'e') | (df_dic["感情"] == 'n')]
keys = df_dic["名詞"].tolist()
values = df_dic["感情"].tolist()
dic = dict(zip(keys, values))

# 各名詞が辞書にあるか確認し、あれば感情とともに配列に格納
# print(results)
results2 = []
for word in results:
    word_score = [] 
    score = dic.get(word) 
    # print(score)
    word_score = (word, score) 
    results2.append(word_score)
# print(results2)

# 結果格納用の配列
None_lists = []
p_lists = []
n_lists = []
e_lists = []
# print(results2)
for result in results2:
    # print(result)
    if result[1] == 'p': p_lists.append(result[0])
    elif result[1] == 'n': n_lists.append(result[0]) 
    elif result[1] == 'e': e_lists.append(result[0]) 
    else:
        None_lists.append(result[0])

print(p_lists)
print(len(p_lists))
print("")
print(n_lists)
print(len(n_lists))
print("")
print(e_lists)
print(len(e_lists))
print("")
print(None_lists)
print(len(None_lists))

