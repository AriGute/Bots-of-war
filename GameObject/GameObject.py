from GameObject.Tag import Tag
from GameObject.Transform import Transform
import pygame
from GameObject.Point import Point

class GameObject:
    # private static id for obj
    __staticId = 0
    deltaTime = None

    def __init__(self, name='unnamed', position=(0, 0)):
        self.id = self.__GenerateId()
        self.name = name
        self.funcRefDict = {}
        self.tag = Tag.types[0]
        self.transform = Transform(position)
        self.img = None
        self.Moving = False
        self.step = 50

    def getTag(self):
        return self.tag

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
        """
        If Game object is not facing the same direction as the givin direction
        then rotate first then wait for the next move command(skip movment).
        if facing the same direction then move in that direction one cell.

        :param direciton: the next direction the game object need to be facing.
        :return: next cell in the tiled map.
        """
        if self.transform.direction == direciton:
            # Rotate to the direction before moving.
            if (self.Moving is False):
                # If not moving(its mean GameObject can take another move)
                pos = self.transform.get_position()
                dir = Transform.direction.get(direciton)
                self.nextStep = (pos[0] + dir[0] * self.step, pos[1] + dir[1] * self.step)
                if self.tag in [Tag.types[1], Tag.types[2]]:
                    # If GameObject is Player or EvilRobot.
                    if self.funcRefDict['cellIsWalkAble'](self.nextStep[0], self.nextStep[1]):
                        # If next cell on the tiledmap is "walkable".
                        self.funcRefDict['rePos'](pos, self.nextStep, self.id, self.tag, self.name)
                        self.Moving = True
                        return self.nextStep
                else:
                    # If GameObject is anything else then Player or evilRobot(exemple: projectile).
                    self.funcRefDict['rePos'](pos, self.nextStep, self.id, self.tag, self.name)
                    self.Moving = True
                    return self.nextStep
                return pos
        else:
            if self.Moving == False:
                self.img = pygame.transform.rotate(self.img, self._getRotate(self.transform.direction, direciton))
                self.transform.direction = direciton

    def _getRotate(self, originDir, targetDir):
        dirDict = {"north": 90, "south": 270, "east": 0, "west": 180}
        originalAngle = dirDict[originDir]
        targetAngle = dirDict[targetDir]
        angle = 0
        while (originalAngle + angle) % 360 != targetAngle:
            angle += 90
        return angle

    def __repr__(self):
        return "ID: {id}, NAME: {n}, POSITION: {p}, TAG: {t}.".format(id=self.id, n=self.name, p=self.transform.get_gridPosition(), t=self.tag)