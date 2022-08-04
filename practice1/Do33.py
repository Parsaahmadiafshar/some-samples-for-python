import mysql.connector
NDatabase = input('Enter name for database===>>')
mydb = mysql.connector.connect(host='localhost', user='root', password='')
#create data base
mycursor = mydb.cursor()
mycursor.execute(f'CREATE DATABASE {NDatabase}')
mycursor.execute(f'use {NDatabase}')
TName = input('Enter Table name for your database ===>>')
columnName = input('Enter one name for your column===>> ')

mycursor.execute(f'CREATE Table {TName} ({columnName} varchar(255)')
password = input('Enter password to insert')
sql = f' INSERT INTO {TName} ({columnName}) VALUES (%s)'
mycursor.executemany(sql, password)
mydb.commit()
