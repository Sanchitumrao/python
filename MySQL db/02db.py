import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mycollege"
    )
#create a table `student` in mycollege database

cursor=conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS student(
          id INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(100),
          MARKS INT
          )"""
    )
print("table  created successfully")
conn.close()
