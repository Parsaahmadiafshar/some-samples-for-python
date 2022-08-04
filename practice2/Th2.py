Num1 = int(input('Number1:'))
Num2 = int(input('Number2:'))
print('===================================')
if Num1 > Num2:
    x = False
    y = True
    Txt1 = 'Number1 is bigger than Number2: {0}'
    print(Txt1.format(y))
    Txt2 = 'Number2 is bigger than Number2: {0}'
    print(Txt2.format(x))
    Txt3 = 'both Numbers are equal: {0}'
    print(Txt3.format(x))
elif Num2 > Num1:
    x = False
    y = True
    Txt1 = 'Number1 is bigger than Number2: {0}'
    print(Txt1.format(x))
    Txt2 = 'Number2 is bigger than Number2: {0}'
    print(Txt2.format(y))
    Txt3 = 'both Numbers are equal: {0}'
    print(Txt3.format(x))
elif Num2 == Num1:
    x = False
    y = True
    Txt1 = 'Number1 is bigger than Number2: {0}'
    print(Txt1.format(x))
    Txt2 = 'Number2 is bigger than Number2: {0}'
    print(Txt2.format(x))
    Txt3 = 'both Numbers are equal: {0}'
    print(Txt3.format(y))