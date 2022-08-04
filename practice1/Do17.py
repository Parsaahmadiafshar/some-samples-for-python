pass1 = input('Enter Ali\'s passwod:')
pass2 = input('Enter Alireza\'s passwod:')
pass3 = input('Enter Mohamad\'s passwod:')
name = input('Enter a name:')
tup1 = ()
x = list(tup1)
x.append(pass1)
x.append(pass2)
x.append(pass3)
j = tuple(x)
if name == 'Ali':
    print(j[0])
elif name == 'Alireza':
    print(j[1])
elif name == 'Mohamad':
    print(j[2])

