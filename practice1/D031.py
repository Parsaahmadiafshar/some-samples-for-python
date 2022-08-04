lst = []
number = input('Enter number to see result ===>> ')
for i in number:
    lst.append(i)
for j in lst:
    x = int(j) * j
    print(f'{j} : ', x)
