from GameObject.Tag import Tag
from GameObject.Transform import Transform
import pygame
from GameObject.Point import Point

class GameObject:
    # private static id for obj
    __staticId = 0;
    deltaTime = None

    def __init__(self, name='unnamed', position=(0, 0)):
        self.id = self.__GenerateId()
        self.name = name
        self.funcRefDict = {}
        self.tag = Tag()
        self.transform = Transform(position)
        self.img = None
        self.Moving = False
        self.step = 50

    def __GenerateId(self):
        """
        private static method to generate uniqe obj id
        :return: uniqe id
        """
        GameObject.__staticId += 1
        return GameObject.__staticId-1

    def update(self, deltaTime):
        """
        this method run every frame
        and should handle all the logic of an object.
        """
        if (self.Moving == True):
            if (self.transform.distance(point=Point((self.nextStep[0], self.nextStep[1]))) > 5):
                pos = self.transform.get_position()
                if pos[0] > self.nextStep[0]:
                    self.transform.set_position((pos[0] - self.speed * deltaTime, pos[1]))
                elif pos[0] < self.nextStep[0]:
                    self.transform.set_position((pos[0] + self.speed * deltaTime, pos[1]))

                if (pos[1] > self.nextStep[1]):
                    self.transform.set_position((pos[0], pos[1] - self.speed * deltaTime))
                elif pos[1] < self.nextStep[1]:
                    self.transform.set_position((pos[0], pos[1] + self.speed * deltaTime))
            else:
                self.transform.set_position(self.nextStep)
                self.nextStep = None
                self.Moving = False

    def draw(self, display_surf):
        if self.img is not None:
            display_surf.blit(self.img, self.transform.get_position())

    def addFunctionRef(self, key, val):
        """
        Add a reffrence to function out of this class.
        :param key: name of function as string
        :param val: the function
        """
        self.funcRefDict[key] = val

    def move(self, direciton):
        if self.Moving == False:
            self.img = pygame.transform.rotate(self.img, self._getRotate(self.transform.direction, direciton))
            self.transform.direction = direciton
        if (self.Moving is False):
            self.Moving = True
            pos = self.transform.get_position()
            dir = Transform.direction.get(direciton)
            self.nextStep = (pos[0] + dir[0] * self.step, pos[1] + dir[1] * self.step)
            self.funcRefDict['rePos'](pos, self.nextStep, self.id, self.tag)
            return self.nextStep

    def _getRotate(self, originDir, targetDir):
        dirDict = {"north": 90, "south": 270, "east": 0, "west": 180}
        originalAngle = dirDict[originDir]
        targetAngle = dirDict[targetDir]
        angle = 0
        while (originalAngle + angle) % 360 != targetAngle:
            angle += 90
        return angle