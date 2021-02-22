from Objects import ExmpleObj

"""
Scene represent some kind of game state(for exemple: main menu, gameMode etc...).
Wen the Main loop is focusing on some scene then for each element in the gameObj list
the main loop should run the obj update function and drawing function.
"""
class Scene:
    def __init__(self):
        self.gameObjectList = []

    def runScene(self):
        for obj in self.gameObjectList:
            obj.update()

    def drawScene(self, display_surf):
        for obj in self.gameObjectList:
            obj.draw(display_surf)
