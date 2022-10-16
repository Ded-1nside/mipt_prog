from math import sqrt
class Vector():
    def __init__(self, x = 0, y = 0, z = 0): #default values are to avoid errors with 1-dim and 2-dim vectors
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __str__(self):
        return "Your vector ({}, {}, {})".format(self.x, self.y, self.z)
    
    def __len__(self): #this method solves the second issue
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def __add__(self, other): # __sub__ function is not neccessary due to vectors' spec
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __nummul__(self, num):
        return Vector(self.x * num, self.y * num, self.z * num)

    def __skmul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    @classmethod
    def vect_inp(cls, string):
        return cls(*string.split(','))