import Point

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
        self.position = Point()
        self.direction = Transform.direction["north"]

    def changeDir(self, direction):
        self.direction = Transform.direction[direction]
