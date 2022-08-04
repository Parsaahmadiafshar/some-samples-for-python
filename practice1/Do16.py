tup1 = ('Dart', 'python', 'c#', 'Html', 'css', 'javascript', 'java')
print(tup1)
print('===================================================================')
x = input('please enter your language to insert in the tuple:')
y = input(' please enter one languge that exist in the tuple to remove that:')
z = int(input('please enter one index:'))
k = input('please enter one language to isert recording to index number:')
j = list(tup1)
j.insert(0, x)
j.remove(y)
j.insert(z, k)
print(tuple(j))




