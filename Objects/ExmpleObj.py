import pygame
from GameObject.GameObject import GameObject

class ExmpleObj(GameObject):
    def __init__(self):
        GameObject.__init__(self,"ExmpleObj")
        self.img = pygame.image.load("Resources/circle.png")
        print(self.img)

    def update(self):
        print("exmple obj is runing now..")