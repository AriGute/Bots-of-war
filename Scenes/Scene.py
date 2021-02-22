from Objects import ExmpleObj

"""
Scene represent some kind of game state(for exemple: main menu, gameMode etc...).
Wen the Main loop is focusing on some scene then for each element in the gameObj list
the main loop should run the obj update function and drawing function.
"""
class Scene:
    def __init__(self):
        self.gameObjectList = []

class ExmpleScene(Scene):
    def __init__(self):
        Scene.__init__()
        self.gameObjectList.append(ExmpleObj)

    def __repr__(self):
        return self.gameObjectList