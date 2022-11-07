# MySQLdbのインポート
import MySQLdb
# スクレイピングデータのインポート
import scraping_yahoonews_topic

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
cursor.execute("DROP TABLE IF EXISTS news_fields")
cursor.execute("DROP TABLE IF EXISTS news_contents")
 
# テーブルの作成
cursor.execute("""CREATE TABLE news_fields(
    id INT(11) AUTO_INCREMENT NOT NULL, 
    news_field VARCHAR(16) NOT NULL, 
    PRIMARY KEY (id)
    )""")

cursor.execute("""CREATE TABLE news_contents(
    id INT(11) AUTO_INCREMENT NOT NULL, 
    news_content VARCHAR(32) NOT NULL, 
    PRIMARY KEY (id)
    )""")

news_fields = scraping_yahoonews_topic.news_fields
news_contents = scraping_yahoonews_topic.news_contents
print(news_fields)
print(news_contents)
for field in news_fields:
    sql = "INSERT INTO news_fields (news_field) VALUES (%s)"
    cursor.executemany(sql, [(field,)])

for content in news_contents:
    sql = "INSERT INTO news_contents (news_content) VALUES (%s)"
    cursor.executemany(sql, [(content,)])
 
# 保存を実行
connection.commit()
 
# 接続を閉じる
connection.close()