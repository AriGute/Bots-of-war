from Scenes.Scene import Scene
from Objects.ExmpleObj import ExmpleObj


class ExmpleScene(Scene):
    def __init__(self, listener):
        Scene.__init__(self, listener)
        self.addGamObj("ExmpleObj", ExmpleObj((100, 100)))

    def update(self):
        pass

    def eventListener(self, event):
        pass
