from GameObject.Point import Point
from math import trunc
import pygame

class Transform:
    w, h = None, None

    direction = {
        "west": (-1, 0),
        "east": (1, 0),
        "south": (0, 1),
        "north": (0, -1),
    }

    def __init__(self, position=(0, 0)):
        self._position = Point(position)
        self.direction = "north"
        self.singleScreenBounds()
        self.step = 50

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

    def inBounds(self, direction):
        """
        Check if position is in the game bounds.
        :param pos: position that need to be checked
        :return: True if in bounds, False if not in game bounds.
        """
        pos = None
        if type(direction) == str:
            pos = self.calcNextPos(direction)
        if type(direction) == tuple:
            pos = direction

        if pos[0] < 0 or pos[0] >= self.w or pos[1] < 0 or pos[1] >= self.h:
            return False
        return True

    def calcNextPos(self, dir=None):
        """
        Calculate the next position with given current position and direction
        to next position.
        :param pos: current position.
        :param dir: direction to next position.
        :return:
        """
        if dir is None:
            return (0, 0)

        pos = self.get_position()
        nextPos = (pos[0] + Transform.direction[dir][0] * self.step,
                   pos[1] + Transform.direction[dir][1] * self.step)
        return nextPos

    def singleScreenBounds(self):
        if Transform.w is None and Transform.h is None:
            Transform.w, Transform.h = pygame.display.get_surface().get_size()

