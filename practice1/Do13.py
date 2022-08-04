list = ['Dena+ Turbo Automated', 'pars ELX Xantia Engine', '206', '207i', 'BMW i8']
print(list)
print('===================================================================')
x = input('please enter one of the cars that exist in list:')
y = input('please enter your favorite car:')
if x in list and y not in list:
    list.remove(x)
    list.insert(0, y)
    print(list)
