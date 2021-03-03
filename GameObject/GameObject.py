from GameObject.Tag import Tag
from GameObject.Transform import Transform
import pygame


class GameObject:
    # private static id for obj
    __staticId = 0;
    deltaTime = None

    def __init__(self, name='unnamed', position=(0, 0)):
        self.name = name
        self.tag = Tag()
        self.transform = Transform(position)
        self.img = None

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

        *need to ovveride*
        """
        raise NotImplementedError

    def draw(self, display_surf):
        if self.img is not None:
            display_surf.blit(self.img, self.transform.get_position())

