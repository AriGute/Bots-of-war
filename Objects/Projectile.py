import pygame
from GameObject.GameObject import GameObject
from GameObject.Transform import Transform

# TODO: projectile destroyed if out of screen bounds
class Projectile(GameObject):

    def __init__(self, position):
        GameObject.__init__(self,"ExampleObj", position)
        self.img = pygame.image.load("Resources/projectile.png")
        self.speed = 30

    def update(self, deltaTime):
        super().update(deltaTime)
        if self.Moving is False:
            self.move(self.transform.direction)


