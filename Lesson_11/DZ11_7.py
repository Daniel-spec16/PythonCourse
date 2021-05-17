class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        sum = f"{self.a+other.a}+({self.b+other.b})i"
        return sum

    def __mul__(self, other):
        mul = f"{(self.a * other.a)+(-(self.b * other.b))}+({(self.a * other.b) + (self.b * other.a)})i"
        return mul


complex_1 = ComplexNum(2, -3)
complex_2 = ComplexNum(6, -2)
print(complex_1 * complex_2)
print(complex_1 + complex_2)