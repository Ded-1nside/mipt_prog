class BinTree:
    def __init__(self, value, l = None, r = None):
        self.value = value
        self.l = l
        self.r = r

    def __iter__(self):
        yield self
        if self.l:
            for subtr in self.l:
                yield subtr
        if self.r:
            for subtr in self.r:
                yield subtr
    
    def get_start_val(self):
        return self.value