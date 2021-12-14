#to connect to a specific database
import mysql.connector

connection = mysql.connector.connect(host='localhost',user='root',password='',database='testdb')
print(connection)

"""
SQL FOR CREATING TABLES

CREATE TABLE THEN tablename(
    column1 datatypes constrains,
    column2 datatype constrains
    ...
    column datatypes constrains)
    
    SQL DATATYPES
    INT-integer
    DECIMAL-
    CHAR-string not exceeding 255 characters
    VARCHAR-sttring length max is 65535
    TEXT-sttring length max is 65535
    DATE-yyyy-mm-dd
    DATETIME-yyyy-mm-dd HH:MM:SS
    TIMESTAMP- 
    BLOB
    
    CONSTRAIN/MODIFIERS - rules defining the kind and how the values are going to be stored in the table
    
    NOT NULL - ensure field cannot acept null values
    PRIMARY KEY PK - 
    AUTO INCREMENT - 
    UNIQUE -EG THE EMAIL FIELD
    FOREIGN KEY FK 
"""

sql = """
    CREATE TABLE IF NOT EXISTS persons(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARChAR (50) NOT NULL,
    bith_date DATE,
    phone VARCHAR(16) NOT NULL UNIQUE
    );
"""
#create cursor object
obj=connection.cursor()

obj.execute(sql)

sql2 = """
        INSERT INTO persons(name,bith_date,phone)
        VALUES('Henry','1999-07-12','07524210'),
        ('Henry','1999-07-12','0752453744'),
        ('Henry','1999-07-12','0752875145'),
        ('Henry','1999-07-12','0752426234');
"""
#INSERT DATA INTO A TABLE


#INSERT INTO a table
#column,col2,...coln)
#VALUES(value1,value2,...valueN),--stop here for one record--
#(value1,value2,...valueN

# obj.execute(sql2)
# connection.rollback() #undo the changes
# connection.commit() #save the changes permanently
# connection.close()

#  sch="""
#      CREATE TABLE IF NOT EXIST student(
#      admin.no INT NOT NULL PRIMARY KEY AUTO INCREMENT UNIQUE,
#      name VARCHAR (50) NOT NULL,
#      birth_date DATE,
#      marks INT NOT NULL UNIQUE);
#
# """
# sch2 = """
#     INSERT INTO students(admin.no,name,birth_date,marks)
#     VALUES('6248',')
# """

