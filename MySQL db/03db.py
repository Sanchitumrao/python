import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )
#insert values to table `student`

cursor=conn.cursor()
sql="INSERT INTO student (name,marks)VALUES(%s,%s)"
values=[("Sanchit",75),("Saurabh",90),("Amit",78),("Satyam",87)]
cursor.executemany(sql,values)
conn.commit()
print(cursor.rowcount,"records inserted successfully")
conn.close()

