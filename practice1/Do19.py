x = input('Enter your first name:')
y = input('Enter your last name:')
z = input('Enter your job:')
print('========================================')
x1 = input('Enter your first name:')
y2 = input('Enter your last name:')
z3 = input('Enter your job:')
listdict = {
    'first name': x,
    'last name': y,
    'job': z
}
listdict2 = {
    'first name': x,
    'last name': y,
    'job': z
}
listdict3 ={
    'Ali': listdict,
    'Hossein': listdict2
}
print(listdict3)
