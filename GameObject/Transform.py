from GameObject.Point import Point

class Transform:

    direction = {
        "west": "WEST",
        "east": "EAST",
        "south": "SOUTH",
        "north": "NORTH",
        "nw": "NORTH WEST",
        "ne": "NORTH EAST",
        "se": "SOUTH EAST",
        "sw": "SOUTH WEST"
    }

    def __init__(self):
        self._position = Point()
        self.direction = Transform.direction["north"]

    def changeDir(self, direction):
        self.direction = Transform.direction[direction]

    def get_position(self):
        return (self._position.x, self._position.y)

    def set_position(self, position):
        """
        :param pos: next position as Point
        :return: nothing
        """
        self._position = Point(position)
