from wings import *


class Animal():
    name = ""
    age = None
    spec = None
    info = []


    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = [name, age]
    
    def get_info(self):
        return self.info
    
    def get_spec(self):
        return self.spec

    def set_spec(self, spec):
        self.spec = spec
    
    def set_info(self):
        self.info.append(self.spec)

class Insect(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Zebra(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Dolphin(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Bird(Animal, FeatheredWings):
    def __init__(self, name, age):
        super().__init__(name, age)


class Bat(Animal, WebWings):
    def __init__(self, name, age):
        super().__init__(name, age)


class Fly(Insect, WebWings):
    def __init__(self, name, age):
        super().__init__(name, age)


class ColoradoBug(Insect, WebWings):
    def __init__(self, name, age):
        super().__init__(name, age)
