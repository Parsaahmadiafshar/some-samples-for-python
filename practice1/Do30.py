lst = []
str1 = input('Enter string ===>>')
str1.upper()
lst.append(str1)
str2 = input('Enter string===>>')
str2.upper()
while str2 != 'exit' and 'EXIT':
    lst.append(str2)
    str2 = input('Enter string===>>')
    str2.upper()
filename = input('Enter filename like this(filename.txt)====>> ')

file = open(filename, 'w')
for i in lst:
    file.write(i + '  ')
file = open(filename, 'r')
print(file.read())
file.close()
