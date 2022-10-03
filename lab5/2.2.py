class Mother():
    name = ""


    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name


class Daughter(Mother):
    def set_name(self, n):
        self.name = n


if __name__ == "__main__":
    m = Mother("ААААА")
    d = Daughter("BBBBB")
    d.set_name("QQQQQQQQQQQQQQ")
    m.set_name("ZZZZZZZZZ")
    print(m.get_name())
    print(d.get_name())