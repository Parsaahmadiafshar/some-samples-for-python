num1 = int(input('Enter First number =====>>'))
num2 =int(input('Enter second number =====>>'))
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
if num1 > num2:
    i = num2 + (num1 + 2)
    print(f'num1 after process===>>{num1}')
    print(f'num2 after process===>>{i}')
elif num2 > num1:
    print(f'num1 after process===>>{num1}')
    print(f'num2 after process===>>{num2}')
elif num1 == num2:
    j = num2 + 5
    print(f'mum1 after process===>>{num1}')
    print(f'num2 after process===>>{j}')
