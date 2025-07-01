#connect to mysql

import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )
cursor=conn.cursor()

#create a database `mycollege` in mysql

cursor.execute("CREATE DATABASE IF NOT EXISTS mycollege")
print("DB created successfully")
conn.close()
