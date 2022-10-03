class shape():
    width = 0
    height = 0
    

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_width(self):
        return self.width

    def get_heihgt(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


class triangle(shape):
    area = 0


    def get_area(self):
        return self.area

    def set_area(self):
        self.area = 0.5 * self.height * self.width


class rectangle(shape):
    area = 0


    def get_area(self):
        return self.area
    
    def set_area(self):
        self.area = self.height * self.width


tr = triangle(int(input()), int(input()))
tr.set_area()
print(tr.get_area())
rc = rectangle(int(input()), int(input()))
rc.set_area()
print(rc.get_area())