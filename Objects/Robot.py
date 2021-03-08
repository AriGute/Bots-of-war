import pygame
from GameObject.GameObject import GameObject
from GameObject.Transform import Transform
from Objects.Projectile import Projectile


class Robot(GameObject):
    def __init__(self, name="Robot", position=(0, 0)):
        GameObject.__init__(self,name, position)
        self.img = pygame.image.load("Resources/roboTest.png")
        self.transform.set_position(position)
        self.speed = 13
        self.fireRate = 3
        self.fireTimer = 0
        self.nextStep = None
        self.tag = 'Player'
        self.w, h = pygame.display.get_surface().get_size()


    def update(self, deltaTime):
        super().update(deltaTime)
        if self.fireTimer > 0:
            self.fireTimer -= deltaTime

    def fire(self):
        if self.fireTimer > 0:
            return None
        self.fireTimer = self.fireRate
        pos = self.transform.get_position()
        dir = Transform.direction.get(self.transform.direction)
        spawnPos = (pos[0] + dir[0] * self.step, pos[1] + dir[1] * self.step)
        # Check if projectile try to spawn out of screen bounds
        if spawnPos[0] < 0 or spawnPos[0] >= Transform.w or spawnPos[1] < 0 or spawnPos[1] >= Transform.h:
            return None
        return Projectile(pos)

    def botAi(self, target):
        nextMove = self.transform.get_position()

