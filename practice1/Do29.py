lst = []
num1 = int(input('Enter first number ===>> '))
lst.append(num1)
num2 = input('Enter number(exit is allowed)===>> ')
while num2 != 'exit':
    lst.append(int(num2))
    num2 = input('Enter number(exit is allowed)===>> ')
print(f'{min(lst)} is min number')


