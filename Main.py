import pygame
from Scenes.MainMenuScene import MenuScene

# for any explnation for the code -> http://pygametutorials.wikidot.com/tutorials-basic

class App:
    def __init__(self):
        pygame.display.set_caption('Bots Of War')
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.deltaTime = 0

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.nextScene(MenuScene(self.nextScene))
        self.deltaTime = pygame.time.Clock().tick(30)/100

    def on_event(self, event):
        self.scene.eventListener(event)
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.deltaTime = pygame.time.Clock().tick(30)/100
        self.scene.runScene(self.deltaTime)

    def on_render(self):
        self.clock.tick(self.fps)  # set the frame rate to 30
        self.scene.drawScene(self._display_surf)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def nextScene(self, scene = None):
        self.scene = scene
        self.scene.drawTiledMap(self._display_surf)


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()