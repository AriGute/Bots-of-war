import sys

import pygame

from Scenes.GameScene import GameScene
from Scenes.Scene import Scene


class MenuScene(Scene):
    title = "BOTS OF WAR"

    colorBlack = (0, 0, 0)
    colorBlue = (0, 0, 255)

    def __init__(self, nextSceneListener):
        Scene.__init__(self, nextSceneListener)
        self.display_surf = None
        self.step = 50

        self.Resources = []
        self.Resources.append(pygame.image.load("Resources/ground_mud.png"))
        self.Resources.append(pygame.image.load("Resources/wall.png"))

        self.tiledMap = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.textFont = pygame.font.SysFont('Arial black', 40)
        self.width = None
        self.height = None

    def eventListener(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Clicking on the play button
            if self.width/2-50 < pygame.mouse.get_pos()[0] < self.width/2+50 and self.height/2-50 < pygame.mouse.get_pos()[1] < self.height/2:
                print("Play")
                self.nextScene(GameScene(self.nextScene))

            # Clicking on the About button
            if self.width/2-50 < pygame.mouse.get_pos()[0] < self.width/2+85 and self.height/2+10 < pygame.mouse.get_pos()[1] < self.height/2+50:
                print("About")

            # Clicking on the Quit button
            if self.width/2-50 < pygame.mouse.get_pos()[0] < self.width/2+50 and self.height/2+60 < pygame.mouse.get_pos()[1] < self.height/2+100:
                print("Quit")
                # pygame.quit()
                # sys.exit()

    def drawTiledMap(self, display_surf):
        """
        Draw Tilled map on the display surface once.
        """
        self.display_surf = display_surf
        for j in range(0, len(self.tiledMap)):
            for i in range(0, len(self.tiledMap[0])):
                display_surf.blit(self.Resources[self.tiledMap[j][i]], (self.step * i, self.step * j))

        self.makeButtons()
        self.makeTitle()

    def makeButtons(self):
        self.width = self.display_surf.get_width()
        self.height = self.display_surf.get_height()

        playtext = self.textFont.render('Play', True, self.colorBlue)
        quittext = self.textFont.render('Quit', True, self.colorBlue)
        abouttext = self.textFont.render('About', True, self.colorBlue)

        self.display_surf.blit(playtext, (self.width / 2 - 50, self.height / 2 - 50))
        self.display_surf.blit(abouttext, (self.width / 2 - 50, self.height / 2))
        self.display_surf.blit(quittext, (self.width / 2 - 50, self.height / 2 + 50))

    def makeTitle(self):
        title = self.textFont.render(MenuScene.title, True, MenuScene.colorBlack)
        self.display_surf.blit(title, (self.width / 4 + 50, self.height - 475))

    def update(self):
        pass

