"""
DROP TABLE NAME
"""
import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='',database='testdb')


mycursor=db.cursor()
sql="DROP TABLE persons"
mycursor.execute(sql)
db.commit()

