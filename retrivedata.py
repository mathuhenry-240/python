import mysql.connector

#crete connection to the daatabase
db = mysql.connector.connect(host='localhost',user='root',password='',database='testdb')

#create cursor object
mycursor=db.cursor()

"""
SLECTING DATA FROM A TABLE IN SQL
#selct all the columns
    SELECT * FROM table_name

#select some coumn
    SELECT coumn1,coumn2...FROM table_name
    
#select column based on condition
    SELECT col1,col2, FROM table_name WHERE condtion
    
SELECTING * FROM table_namme LIMIT 5 OFFSET 3 

SELECTING * FROM table_namme LIMIT 5 
"""

# sql = "SELECT * FROM persons" #fetch all
# sql = "SELECT bith_date,phone FROM persons;" #get required cols only
        #ODERING RESULT
sql = "SELECT * FROM persons ;"
# sql = "SELECT * FROM persons WHERE name=%s;"
# jkl=("henry",)


#execute the query
mycursor.execute(sql)
dbdata=mycursor.fetchall()

for datum in dbdata:
    print(datum)