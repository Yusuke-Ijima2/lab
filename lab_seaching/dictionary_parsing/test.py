import pandas as pd

df_dic = pd.read_csv('pn.csv.m3.120408.trim', sep='\t', names=("名詞", "感情", "動詞句"), encoding='utf-8')
# 辞書の中身と感情の中身を確認
print(df_dic)
print(df_dic["感情"].value_counts())
# 感情のうち、p/e/nの項目のみを抽出
df_dic = df_dic[(df_dic["感情"] == 'p') | (df_dic["感情"] == 'e') | (df_dic["感情"] == 'n')]
# 動詞句を削除
df_dic = df_dic.iloc[:,0:2]
keys = df_dic["名詞"].tolist()
values = df_dic["感情"].tolist()
dic = dict(zip(keys, values))

print(dic)