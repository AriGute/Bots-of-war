import pygame
from GameObject.GameObject import GameObject
from GameObject.Transform import Transform

class Projectile(GameObject):

    def __init__(self, position):
        GameObject.__init__(self,"ExampleObj", position)
        self.img = pygame.image.load("Resources/projectile.png")
        self.speed = 5

    def update(self, deltaTime):
        # TODO: find a way to do static delta time to all GameObjects
        pos = self.transform.get_position()
        dir = Transform.direction[self.transform.direction]
        nextPos = (pos[0] + dir[0]*deltaTime*self.speed, pos[1] + dir[1]*deltaTime*self.speed)
        self.transform.set_position(nextPos)

