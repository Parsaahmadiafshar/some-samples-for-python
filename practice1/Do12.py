a = input('student1 name:')
b = input('student2 name:')
c = input('student3 name:')
d = input('student1 score:')
e = input('student2 score:')
f = input('student3 score:')
list1 = []
list2 = []
list1.append(a)
list1.append(b)
list1.append(c)
list2.append(d)
list2.append(e)
list2.append(f)
list1.extend(list2)
print(list1)