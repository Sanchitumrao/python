import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )
#update data in student table

cursor=conn.cursor()
sql="UPDATE student SET marks =%s WHERE name=%s"
value=(80,"Sanchit")
cursor.execute(sql,value)
conn.commit()
print(cursor.rowcount,"records updated successfully")
conn.close()