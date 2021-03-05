from GameObject.Point import Point
from math import trunc

class Transform:

    direction = {
        "west": (-1, 0),
        "east": (1, 0),
        "south": (0, 1),
        "north": (0, -1),
    }

    def __init__(self, position=(0, 0)):
        self._position = Point(position)
        self.direction = "north"

    def changeDir(self, direction):
        self.direction = Transform.direction[direction]

    def get_position(self):
        return (self._position.x, self._position.y)

    def get_gridPosition(self):
        step = 50
        pos = self.get_position()
        gridPos = (trunc(pos[0]/step), trunc(pos[1]/step))
        return gridPos

    def set_position(self, position):
        """
        :param pos: next position as Point
        :return: nothing
        """
        self._position = Point(position)

    def distance(self, point):
        return self._position.distance(point)