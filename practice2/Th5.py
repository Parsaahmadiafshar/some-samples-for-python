Salary = float(input('Enter salary:'))
print('======================================')
Bime = Salary * 0.07 # mohasebe bime
Bime1 = Salary - Bime
x = 'BIME:{0}'
print(x.format(Bime))
Maliat = Bime1 * 0.1# mohasebe maliat
y = 'MALIAT:{0}'
print(y.format(Maliat))
Sum = Bime + Maliat
Income = Salary - Sum
Txt = 'INCOME SALARY IS : {0}'
print(Txt.format(Income))
