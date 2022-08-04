class person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def info1(self):
        return [self.fname, self.lname]
    def showInfo(self):
       return f'Hello {self.fname} {self.lname} you are {self.age} years old'
    def happybirthday(self):
        print(f'Happy birthday {self.fname} {self.lname} your new age is {self.age+1} ')

p1 = person("John", 'jjjj', 36)
print(p1.showInfo())
print(p1.happybirthday())






