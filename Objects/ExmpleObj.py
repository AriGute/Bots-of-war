from GameObject import GameObject
import pygame

class ExmpleObj(GameObject):
    def __init__(self):
        super().__init__(self, "Exemple obj", id=0)
        self.img = pygame.image.load("Resources/circle.png")