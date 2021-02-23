import pygame
from GameObject.GameObject import GameObject

class Ground(GameObject):
    def __init__(self, position):
        GameObject.__init__(self,"Ground", position)
        self.img = pygame.image.load("Resources/ground_mud.png")
        self.transform.set_position((0,0))

    def update(self):
        print("ground")