import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=KOMAL\SQLEXPRESS;'
                      'Database=biodb;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM products')

for i in cursor:
    print(i)