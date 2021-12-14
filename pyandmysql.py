#import mysql.connector
import mysql.connector

#create a connection
#connection_object=mysql.connector.connect(host,user,pass)
connection = mysql.connector.connect(host='localhost',user='root',password='')
#print(connection)
#creating a database

""""
sql for creating a database
"CREATE A DATABASE databasename"

"""

#create cursor object
#connection.cursor()

cursor = connection.cursor()

#sql = "CREATE DATABASE testDb"
sql = "CREATE DATABASE IF NOT EXISTS testDb"

#tell to execute the sql
cursor.execute(sql)

#show all the databases

#sql - " show databases"

sql1 = "show databases"
cursor.execute(sql1)

for database in cursor:
    print(database)

#select a specific database
#sQL - "USE DATABASE NAME"

sql2 = "use testdb"
cursor.execute(sql2)

