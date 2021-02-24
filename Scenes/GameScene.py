import pygame

from math import trunc
from Scenes.Scene import Scene
from Objects.Ground import Ground
from Objects.Wall import Wall
from Objects.Robot import Robot

# TODO: draw over the last pixels the robot was
class GameScene(Scene):
    def __init__(self, listener):
        Scene.__init__(self, listener)
        self.step = 50;
        self.display_surf = None

        self.Resources = []
        self.Resources.append(pygame.image.load("Resources/ground_mud.png"))
        self.Resources.append(pygame.image.load("Resources/wall.png"))

        self.tiledMap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.addGamObj("Robot", Robot((200, 100)))

    def eventListener(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.redraw(self.getGameObj("Robot").transform.get_position())
            self.getGameObj("Robot").transform.set_position(pygame.mouse.get_pos())

    def drawTiledMap(self, display_surf):
        """
        Draw Tilled map on the display surface once.
        """
        self.display_surf = display_surf
        print(self.tiledMap[0][0])
        for j in range(0, len(self.tiledMap)):
            for i in range(0, len(self.tiledMap[0])):
                print(str(j) + ", " + str(i))
                display_surf.blit(self.Resources[self.tiledMap[j][i]], (self.step * i, self.step * j))

    # TODO: fix crash if objPos is near app edges
    def redraw(self, objPos):
        """
        Used if gameObject from the Scene is gonna change position.
        Redraw override the last tiled map cells the gameObject was over in his last position.
        :param objPos:
        :return:
        """
        x = trunc(objPos[0] / self.step)
        y = trunc(objPos[1] / self.step)
        for pos in [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]:
            self.display_surf.blit(self.Resources[self.tiledMap[pos[1]][pos[0]]], (self.step * pos[0], self.step * pos[1]))

