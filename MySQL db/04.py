import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )
#fetch data from student table
cursor=conn.cursor()
cursor.execute("SELECT *FROM student")
rows=cursor.fetchall()
for row in rows:
    print(row)

print(cursor.rowcount,"data fetched successfully")
conn.close()