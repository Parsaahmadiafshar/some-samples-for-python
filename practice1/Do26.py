import os
x = input('Enter the file name ==>')
y = input('Enter user name==>')
z = input('Enter your password==>')
if os.path.exists(x):
    f = open(x, 'w')
    f1 = f.write(f'user name is ==> {y}')
    f2 = f.write(f'password is ==> {z}')
else:
    f = open(x, 'w')
    f1 = f.write(f'user name is ==> {y}')
    f2 = f.write(f'password is ==> {z}')

