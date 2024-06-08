from .Animal import Animal

class Rys(Animal):

    def __init__(self, rys=None, position=None, world=None):
        super(Rys, self).__init__(rys, position, world)

    def clone(self):
        return Rys(self, None, None)

    def initParams(self):
        self.power = 6
        self.initiative = 5
        self.liveLength = 18
        self.powerToReproduce = 14
        self.sign = 'R'
