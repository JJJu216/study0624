import mysql.connector

print("建立資料庫連線中")

cnx=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="dbuser",
    password="1234",
    database="prize"
)
print("透過連線取得 cursor")
dbcursor=cnx.cursor()
print("執行 insert")
insertSQL="insert into lottery(n1,n2,n3,n4,n5,n6) vallues(%s,%s,%s,%s,%s,%s)"

parserdata=(6,11,20,31,34,38)

dbcursor.execote(insertSQL,parserdata)
print("完成交易")
cnx.commit()

dbcursor.close()
cnx.close()