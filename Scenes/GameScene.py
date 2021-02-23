import pygame
from Scenes.Scene import Scene
from Objects.Ground import Ground
from Objects.Wall import Wall
from Objects.Robot import Robot

# TODO: like camera witch represent the offset of all the obj in the game
class GameScene(Scene):
    def __init__(self, listener):
        Scene.__init__(self, listener)
        self.gameObjectList.append(Ground((0, 0)))
        self.gameObjectList.append(Robot((200, 100)))
        self.initWalls()

    def eventListener(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())


    def initWalls(self):
        for i in range(4):
            self.gameObjectList.append(Wall((100, 100+i*100)))
        for i in range(4):
            self.gameObjectList.append(Wall((600, 100+i*100)))
        for i in range(2):
            self.gameObjectList.append(Wall((300+i*100, 300)))
        for i in range(2):
            self.gameObjectList.append(Wall((300+i*100, 200)))