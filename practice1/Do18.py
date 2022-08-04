txt = input('Enter your string:')
x = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
j = {}
y = list(j)
for i in txt:
    if i in x:
        y.append(i)
print(set(y))


