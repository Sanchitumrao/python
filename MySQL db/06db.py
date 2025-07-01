import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )
#delete data in table
cursor=conn.cursor()
sql="DELETE FROM student WHERE name=%s"
value=("Amit",)
cursor.execute(sql,value)
conn.commit()
print(cursor.rowcount,"records deleted successfully")
conn.close()