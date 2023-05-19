import mysql.connector
num=mysql.connector.connect(host="localhost",password="root",user="root")
if num.is_connected():
    print("connection established")