import pygame

from GameObject import GameObject
from Scenes.ExempleScene import ExmpleScene

# for any explation for the code -> http://pygametutorials.wikidot.com/tutorials-basic

class App:
    def __init__(self):
        pygame.display.set_caption('Bots Of War')
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600

        self.clock = pygame.time.Clock()

        self.scene = ExmpleScene()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.clock.tick(30)  # set the frame rate to 30

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    # TODO: understand python casting and how to use the fucking class........
    def on_loop(self):
        self.scene.runScene()

    def on_render(self):
        self.scene.drawScene(self._display_surf)

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

    # TODO: add method to Scene that throw exeption and if Main catch the exeption that mean the current Scene is ended.


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()