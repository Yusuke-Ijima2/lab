# MySQLdbのインポート
import MySQLdb
# スクレイピングデータのインポート
import scraping
 
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
    news_title VARCHAR(255) NOT NULL, 
    news_url VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id)
    )""")

news_title = scraping.news_title
news_url = scraping.news_url
for i in range(len(news_title)):
    # データの追加
    sql = "INSERT INTO news_list (news_title, news_url) VALUES (%s, %s)"
    cursor.execute(sql, (news_title[i], news_url[i]))


# 一覧の表示
cursor.execute("SELECT * FROM news_list")
 
for row in cursor:
    print(row)
 
 
# 保存を実行
connection.commit()
 
# 接続を閉じる
connection.close()