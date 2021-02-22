from Scenes.Scene import Scene
from Objects.ExmpleObj import ExmpleObj

class ExmpleScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.gameObjectList.append(ExmpleObj())

    def __repr__(self):
        return self.gameObjectList
