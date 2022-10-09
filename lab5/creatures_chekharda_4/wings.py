class Wings():
    _type = None
    flapping = False

    
    def __init__(self, type):
        self._type = type

    def i_believe_i_can_fly(self):
        self.flapping = True
        print("I'm flying!")


class FeatheredWings(Wings):
    def __init__(self):
        super().__init__(type="feathered")

    def i_believe_i_can_fly(self): #kinda little Easter Egg
        print("kurlik", end=' ')
        return super().i_believe_i_can_fly()


class WebWings(Wings):
    def __init__(self):
        super().__init__(type="webbed")
    
    def i_believe_i_can_fly(self):
        print("bzzzz", end=" ")
        return super().i_believe_i_can_fly()