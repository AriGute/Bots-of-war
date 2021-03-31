import pygame
from GameObject.GameObject import GameObject

class Projectile(GameObject):

    def __init__(self, position, tag):
        GameObject.__init__(self,"ExampleObj", position)
        self.img = pygame.image.load("Resources/projectile.png")
        self.speed = 40
        self.tag = 'Projectile'
        self.name = 'Projectile'
        self.damage = 10
        self.source = tag

    def update(self, deltaTime):
        super().update(deltaTime)
        if self.Moving is False:
            self.move(self.transform.direction)


