from Scenes.Scene import Scene
from Objects.ExmpleObj import ExmpleObj

class ExmpleScene(Scene):
    def __init__(self, listener):
        Scene.__init__(self, listener)
        self.gameObjectList.append(ExmpleObj((100,100)))

