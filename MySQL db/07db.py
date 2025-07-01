import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )
cursor=conn.cursor()
# delete table student
cursor.execute("Drop table if exists student")
conn.commit()
print("table dropped successfully")
conn.close()