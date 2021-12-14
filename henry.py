import mysql.connector
connection = mysql.connector.connect(host='localhost',user='root',password='',database='newwork')
print(connection)

sql = """
    CREATE TABLE IF NOT EXISTS customers(
    customerid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    customername VARChAR (50) NOT NULL,
    phone VARCHAR(16) NOT NULL UNIQUE,
    Address VARCHAR(16),
    City VARCHAR(16),
    total VARCHAR(16)
    );
"""
obj = connection.cursor()
obj.execute(sql)

sql2 = """
    INSERT INTO customers(customername,phone,Address,city,total)
    VALUES('henry','0758987514','1234','rio','200000'),
    ('edith','0758987514','1234','rio','200000'),
    ('peter','0758457893','1568','tokyo','200000'),
    ('joseph','073456788','18987','berlin','200000'),
    ('vivian','071234567','12009','denver','200000');
"""

obj.execute(sql2)
connection.commit()
connection.close()