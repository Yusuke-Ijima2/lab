# MySQLdbのインポート
import MySQLdb

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

sql = "SELECT * FROM news_list WHERE news_title LIKE %s"
param =  ('海%',)

cursor.execute(sql, param)

for row in cursor:
    print(row)