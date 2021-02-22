import pygame

from GameObject import Tag
from GameObject import Transform



class GameObject:
    # private static id for obj
    __staticId = 0;

    def __init__(self, name='unnamed'):
        self.id = self.__GenerateId()
        self.name = name
        self.tag = Tag()
        self.transform = Transform()
        self.img = None

    def __GenerateId(self):
        """
        private static method to generate uniqe obj id
        :return: uniqe id
        """
        GameObject.__staticId += 1
        return GameObject.__staticId-1

    def update(self):
        pass


class ExmpleObj(GameObject):
    def __init__(self):
        GameObject.__init__("ExmpleObj")
        self.img = pygame.image.load("Resources/circle.png")

    def update(self):
        print("emple obj is runing now..")