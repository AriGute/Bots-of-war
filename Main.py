import pygame

from GameObject import GameObject
from Scenes import Scene

# for any explation for the code -> http://pygametutorials.wikidot.com/tutorials-basic

class App:
    def __init__(self):
        pygame.display.set_caption('Bots Of War')
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600

        self.sceneList = []
        self.currentScene = 0;

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    #     running exmple scene
        self.sceneList.append(Scene.ExmpleObj)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    # TODO: understand python casting and how to use the fucking class........
    def on_loop(self):
        for gameObject in Scene.ExmpleObj(self.sceneList[self.currentScene]):
            gameObject.update()

    def on_render(self):
        for gameObject in self.sceneList[self.currentScene]:
            self._display_surf.blit(gameObject.img, gameObject.transform.position)

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
    def next_scene(self):
        self.currentScene += 1
        if self.sceneList[self.currentScene] is None:
            pygame.quit()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()