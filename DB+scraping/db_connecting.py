# MySQLdbのインポート
import MySQLdb
# スクレイピングデータのインポート
import scraping_yahoonews_topic
# csv出力
import csv

# データベースへの接続とカーソルの生成
connection = MySQLdb.connect(
    host='localhost',
    user='lab_user',
    password='d9rQ9uBa#',
    db='LAB_DB',
# テーブル内部で日本語を扱うために追加
    charset='utf8'
)
cursor = connection.cursor()
 
# テーブルの初期化
cursor.execute("DROP TABLE IF EXISTS news_list")
 
# テーブルの作成
cursor.execute("""CREATE TABLE news_list(
    id INT(11) AUTO_INCREMENT NOT NULL, 
    news_field VARCHAR(16) NOT NULL, 
    news_content VARCHAR(32) NOT NULL, 
    PRIMARY KEY (id)
    )""")

news_fields = scraping_yahoonews_topic.news_fields
news_contents = scraping_yahoonews_topic.news_contents
flag = 0
for i in range(1,len(news_contents)):
    if i % 8 == 0: flag += 1
    for j in range(len(news_fields)):
        if flag == j:n = news_fields[flag]
    
    # データの追加
    sql = "INSERT INTO news_list (news_field, news_content) VALUES (%s, %s)"
    cursor.execute(sql, (n, news_contents[i]))

# 保存を実行
connection.commit()
# 接続を閉じる
connection.close()