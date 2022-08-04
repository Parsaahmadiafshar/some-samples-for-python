import mysql.connector
x1 = input('Enter your name===>>')
x2 = input('Enter your last name===>>')
x3 = input('Enter your age===>>')
x4 = input('Enter your job===>>')
x5 = input('Enter your phone number===>>')
mydb = mysql.connector.connect(host='localhost', user='root', password='')
#create data base
mycursor = mydb.cursor()
mycursor.execute(f'CREATE DATABASE customers')
mycursor.execute(f'use customers')
mycursor.execute(f'CREATE Tamble  customers (fistname varchar(255), lastname varchar(255), age varchar(255),job varchar(255), phonenumber varchar(255))')
sql = f' INSERT INTO customers (fistname, lastname, age, job, phonenumber) VALUES (%s, %b, %c , %j, %l)'
val =(x1, x2, x3, x4, x5)
mycursor.execute(sql, val)
