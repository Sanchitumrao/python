#connect python to mysql
#run command 
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )
# check connection
if conn.is_connected():
    print("connected to my sql server")
conn.close()