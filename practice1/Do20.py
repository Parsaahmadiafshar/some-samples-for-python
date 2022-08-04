list1 = []
def max():
    if i > j:
        return i

while True:
    x = int(input('enter your number ==> '))
    l = input('do you want exit: if yes write exit if not wirte no ==> ')
    list1.append(x)
    if l == 'exit':
        break
print(list1)
for i in list1:
    for j in list1:
        max()

print(f'{i} is bigger than all')