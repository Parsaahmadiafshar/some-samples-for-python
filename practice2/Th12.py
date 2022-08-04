x = int(input('Enter first number ===>>'))
y = int(input('Enter second number ===>>'))
class math():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def multi(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2
M1 = math(x, y)
print(M1.sum())
print(M1.sub())
print(M1.multi())
print(M1.div())



