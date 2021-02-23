import pygame
from GameObject.GameObject import GameObject

class Robot(GameObject):
    def __init__(self, position):
        GameObject.__init__(self,"Robot", position)
        self.img = pygame.image.load("Resources/roboTest.png")
        self.transform.set_position(position)

    def update(self):
        pass

