import pygame
from GameObject.GameObject import GameObject
from GameObject.Transform import Transform
from Objects.Projectile import Projectile


class Robot(GameObject):
    def __init__(self, position):
        GameObject.__init__(self,"Robot", position)
        self.img = pygame.image.load("Resources/roboTest.png")
        self.transform.set_position(position)
        self.speed = 10
        self.fireRate = 3
        self.fireTimer = 0
        self.nextStep = None


    def update(self, deltaTime):
        super().update(deltaTime)
        if self.fireTimer > 0:
            self.fireTimer -= deltaTime

    def fire(self):
        if self.fireTimer > 0:
            return None
        self.fireTimer = self.fireRate
        return Projectile(self.transform.get_position())


