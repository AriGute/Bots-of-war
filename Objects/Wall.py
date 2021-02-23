import pygame
from GameObject.GameObject import GameObject

class Wall(GameObject):
    def __init__(self, position):
        GameObject.__init__(self,"Wall", position)
        self.img = pygame.image.load("Resources/wall.png")
        self.transform.set_position(position)

    def update(self):
        pass

