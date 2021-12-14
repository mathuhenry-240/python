import mysql.connector

#crete connection to the daatabase
db = mysql.connector.connect(host='localhost',user='root',password='',database='testdb')

#create cursor object
mycursor=db.cursor()

"""
DELETING FROM table_name WHERE CONDITION 

"""

sql ="DELETE FROM persons WHERE id=4;"
mycursor.execute(sql)
db.commit()
