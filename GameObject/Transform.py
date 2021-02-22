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

    def __init__(self, point):
        self._position = Point()
        self.direction = Transform.direction["north"]

    def changeDir(self, direction):
        self.direction = Transform.direction[direction]

    def get_position(self):
        return (self.position.x, self.position.y)

    def set_position(self, pos):
        """
        :param pos: next position as Point
        :return: nothing
        """
        self.Point.x = pos.x
        self.Point.y = pos.y