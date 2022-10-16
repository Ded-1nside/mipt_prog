from math import sqrt
class Complex():
    def __init__(self, real, im):
        self.real = real
        self.im = im
    
    @classmethod
    def compl_inp(cls, string):
        string = string.replace('i', '')
        if '+' in string:
            string = string.split('+')
        else:
            string = string.split('-')
        return cls(float(string[0]), float(string[1]))
    
    def __abs__(self):
        return sqrt(self.real ** 2 + self.im ** 2)
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.im + other.im)
    
    def __sub__(self, other):
        return Complex(self.real + other.real, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.im * other.im, self.im * other.real + self.real * other.im)

    def __truediv__(self, other):
        return Complex((self.real * other.real + self.im * other.im)/(other.im * other.im + other.real * other.real), (self.real * other.im + self.im * other.real)/(other.im * other.im + other.real* other.real))