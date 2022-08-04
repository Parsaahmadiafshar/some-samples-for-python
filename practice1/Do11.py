x = input('please enter first language:')
y = input('please enter second language:')
z = input('please enter third language:')
list = ['python', 'c++', 'c', 'c#', 'F#', 'VB', 'Dart', 'R', 'Rust']
list.append(x)
list.insert(0, y)
list.insert(2, z)
print(list)
