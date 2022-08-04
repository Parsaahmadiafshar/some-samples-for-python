import os
filename = input('enter file name ====>>')
if os.stat(filename+'.txt').st_size != 0:
    f = open(filename+'.txt', 'r')
    print(f.read())
    f.close()
else:
    txt = input('enter something to insert in file ===>>')
    f = open(filename+'.txt', 'w')
    print(f.write(txt))
    f.close()
