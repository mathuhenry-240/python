import mysql.connector
connection = mysql.connector.connect(host='localhost',user='root',password='',database='newwork')
print(connection)

sql = """
    CREATE TABLE IF NOT EXISTS berlin(
    customerid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    customername VARChAR (50) NOT NULL,
    phone VARCHAR(16) NOT NULL UNIQUE,
    );
"""
obj = connection.cursor()
obj.execute(sql)

sql2 = """
    INSERT INTO customers(customername,phone)
    VALUES('henry','0758987514'),
    ('edith','0758987514'),
    ('peter','0758457893'),
    ('vivian','071234567');
"""
obj.execute(sql2)
connection.commit()
connection.close()