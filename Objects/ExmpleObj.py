import pygame
from GameObject.GameObject import GameObject
class ExmpleObj(GameObject):
    def __init__(self):
        GameObject.__init__("ExmpleObj")
        self.img = pygame.image.load("Resources/circle.png")

    def update(self):
        print("emple obj is runing now..")