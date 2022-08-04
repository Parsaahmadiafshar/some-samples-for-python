x = input('Enter the number ===>> ')

if int(x) >= 1 and int(x) < 9:
    for i in range(1, int(x)+1):
        print(str(i)*i)
else:
      print('please Enter the number between 1-9')
