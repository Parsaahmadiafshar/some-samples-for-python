import mysql.connector
database = input('Enter your database name ===>>')
table = input('Enter your Table name ===>>')
email = input('Enter your Email address ===>>')
user = input('Enter your user name ====>>')
password = input('Enter your password ===>>')
mydb = mysql.connector.connect(host="localhost", user="root", password="")
# Creat Database
mycursor = mydb.cursor()
mycursor.execute(f"CREATE DATABASE {database}")
mycursor.execute(f'use {database}')
mycursor.execute(f"CREATE TABLE {table} (email VARCHAR(255), username VARCHAR(255), password VARCHAR(60))")
sql = f"INSERT INTO {table} (email, username, password) VALUES (%s, %s, %s)"
val = (email, user, password)
mycursor.execute(sql, val)
mydb.commit()
# print(mycursor.rowcount, "was inserted.")

