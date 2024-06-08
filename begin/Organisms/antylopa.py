from .Sheep import Sheep
from .rys import Rys
from Action import Action
from ActionEnum import ActionEnum
from Position import Position

class Antylopa(Sheep):

    def __init__(self, antylopa=None, position=None, world=None):
        super(Antylopa, self).__init__(antylopa, position, world)

    def clone(self):
        return Antylopa(self, None, None)

    def initParams(self):
        self.power = 4
        self.initiative = 3
        self.liveLength = 11
        self.powerToReproduce = 5
        self.sign = 'A'

    def action(self):
        rys_positions = [pos for pos in self.world.getNeighboringPositions(self.position) if isinstance(self.world.getOrganismFromPosition(pos), Rys)]

        if rys_positions:
            rys_position = rys_positions[0]
            escape_position = self.calculate_escape_position(rys_position)
            if escape_position and self.world.positionOnBoard(escape_position) and not self.world.getOrganismFromPosition(escape_position):
                return [Action(ActionEnum.A_MOVE, escape_position, 0, self)]
            else:
                return [Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self.world.getOrganismFromPosition(rys_position))]
        else:
            return super(Antylopa, self).action()

    def calculate_escape_position(self, rys_position):
        dx = self.position.x - rys_position.x
        dy = self.position.y - rys_position.y
        escape_x = self.position.x + (2 if dx > 0 else -2 if dx < 0 else 0)
        escape_y = self.position.y + (2 if dy > 0 else -2 if dy < 0 else 0)
        return Position(xPosition=escape_x, yPosition=escape_y)
