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

# テーブルの初期化
cursor.execute("DROP TABLE IF EXISTS category_list")

# テーブルの作成
cursor.execute("""CREATE TABLE category_list(
    id INT(11) AUTO_INCREMENT NOT NULL, 
    name VARCHAR(30) NOT NULL ,
    age INT(3) NOT NULL,
    PRIMARY KEY (id)
    )""")

# データの追加
cursor.execute("""INSERT INTO category_list (name, age)
    VALUES ('タロー', '25'),
    ('ジロー', '23'),
    ('サブロー', '21')
    """)

# 一覧の表示
cursor.execute("SELECT * FROM category_list")

for row in cursor:
    print(row)

print('DB登録成功')

# 保存を実行
connection.commit()

# 接続を閉じる
connection.close()