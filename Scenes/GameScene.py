import pygame
from math import trunc
from Scenes.Scene import Scene
from Objects.Robot import Robot
from Objects.Projectile import Projectile

# TODO: create function that clear the memory properly.
class GameScene(Scene):

    def __init__(self, nextSceneListener):
        Scene.__init__(self, nextSceneListener)
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
           print("\n")


        if event.type == pygame.KEYDOWN:
            if self.getGameObj("Robot").Moving != True:
                robot = self.getGameObj("Robot")
                robotNextPos = None
                Projectile = None
                if event.key == pygame.K_LEFT:
                    robotNextPos = robot.move("west")
                elif event.key == pygame.K_RIGHT:
                    robotNextPos = robot.move("east")
                elif event.key == pygame.K_UP:
                    robotNextPos = robot.move("north")
                elif event.key == pygame.K_DOWN:
                    robotNextPos = robot.move("south")
                elif event.key == pygame.K_SPACE:
                    Projectile = self.getGameObj("Robot").fire()
                    if Projectile is not None:
                        self.addGamObj("Projectile", Projectile)
                        Projectile.move(robot.transform.direction)




    def update(self, deltaTime):
        pass
