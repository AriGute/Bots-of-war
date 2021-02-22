from math import sqrt


class Point:

    # The Initial point set to (x,y) = (0,0)
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Returns the distance of 2 points in a tuple -> (x,y)
    # Manhattan distance
    def manhattanDistance(self, other):
        dist = (self.x - other.x, self.y - other.y)
        return dist

    # Returns the distance using the Pythagorean theorem -> x^2 + y^2 = z^2 (Integer Value).
    # Using the tuple returned from manhattanDistance() method, dist[0] = x, dist[1] = y.
    def distance(self, other):
        dist = self.manhattanDistance(other)
        return sqrt(dist[0] ** 2 + dist[1] ** 2)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + " )"

