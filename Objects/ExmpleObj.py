import pygame
from GameObject.GameObject import GameObject

class ExmpleObj(GameObject):
    def __init__(self, position):
        GameObject.__init__(self,"ExmpleObj", position)
        self.img = pygame.image.load("Resources/circle.png")
        self.transform.set_position((100,100))

    def update(self):
        print("exmple obj is runing now..")
        print(self.transform.get_position())