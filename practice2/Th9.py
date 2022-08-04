i = 0
lst = []
num1 = int(input('Enter yor number ====>>'))
lst.append(num1)
while True:
        num2 = input('Enter yor number ====>>')
        if num2 == 'exit':
              break
        lst.append(num2)
for j in lst:
    i = int(j) + i
print(f'Total ===>>{i}')



