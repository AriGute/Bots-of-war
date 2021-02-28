import pygame
from math import trunc

from Scenes.Scene import Scene
from Objects.Robot import Robot

class GameScene(Scene):
    def __init__(self, listener):
        Scene.__init__(self, listener)
        self.step = 50;
        self.display_surf = None
        self.Resources.append(pygame.image.load("Resources/ground_mud.png"))
        self.Resources.append(pygame.image.load("Resources/wall.png"))
        self.tiledMap = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.addGamObj("Robot", Robot((200, 400)))

    def eventListener(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
           for i in self.takeSnapShot():
               print(i)

        if event.type == pygame.KEYDOWN:
            if self.getGameObj("Robot").walking != True:
                robotNextPos = None
                if event.key == pygame.K_LEFT:
                    robotNextPos = self.getGameObj("Robot").move("west", self.step)
                elif event.key == pygame.K_RIGHT:
                    robotNextPos = self.getGameObj("Robot").move("east", self.step)
                elif event.key == pygame.K_UP:
                    robotNextPos = self.getGameObj("Robot").move("north", self.step)
                elif event.key == pygame.K_DOWN:
                    robotNextPos = self.getGameObj("Robot").move("south", self.step)

                newPos = robotNextPos
                oldPos = self.getGameObj("Robot").transform.get_position()
                x1 = trunc(newPos[0] / self.step)
                y1 = trunc(newPos[1] / self.step)
                x2 = trunc(oldPos[0] / self.step)
                y2 = trunc(oldPos[1] / self.step)
                self.tiledMap[y1][x1] = 2
                self.tiledMap[y2][x2] = 0

    def update(self):
        pass


