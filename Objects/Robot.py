import pygame
from GameObject.GameObject import GameObject
from GameObject.Transform import Transform
from Objects.Projectile import Projectile


class Robot(GameObject):
    def __init__(self, position):
        GameObject.__init__(self,"Robot", position)
        self.img = pygame.image.load("Resources/roboTest.png")
        self.transform.set_position(position)
        self.speed = 5
        self.nextStep = None


    def update(self, deltaTime):
        super().update(deltaTime)

    def fire(self):
        print("Fire!")
        print(self.transform.get_position())
        return Projectile(self.transform.get_position())


