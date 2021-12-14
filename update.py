import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='',database='testdb')


tap=db.cursor()
sql="UPDATE persons SET  name='Ethan', phone='0789765433' WHERE id=1"
tap.execute(sql)
db.commit()