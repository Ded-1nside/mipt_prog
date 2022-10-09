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


class Zebra(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Dolphin(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)



if __name__ == "__main__":
    zeb = Zebra("Олег", 21)
    delp = Dolphin("Игорь", 10)
    zeb.set_spec("Зёбра")
    zeb.set_info()
    delp.set_spec("Дельфин")
    delp.set_info()
    print(zeb.get_info())
    print(delp.get_info())
