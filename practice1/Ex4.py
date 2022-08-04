string1 = input('please Enter the string ====>> ')
string1 = string1.lower()
list1 = []
for i in string1:
    x = str(i) + ':', str(string1.count(i))
    list1.append(x)

list2 = list1.copy()
res = [*set(list2)]
result = list(res)
for j in result:
    print(j)





