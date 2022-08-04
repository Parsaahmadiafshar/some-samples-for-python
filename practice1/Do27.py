lst = []
x = input('Enter your string:')
lst.append(x)
while True:
    y = input('enter your string:')
    if y != 'exit':
      lst.append(y)
    if y == 'exit':
        break
f = open('strings.txt', 'w')
for j in lst:
    str1 = f.write(j+" ")
print(str1)
