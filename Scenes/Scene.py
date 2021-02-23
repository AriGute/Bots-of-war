"""
Scene represent some kind of game state(for exemple: main menu, gameMode etc...).
Wen the Main loop is focusing on some scene then for each element in the gameObj list
the main loop should run the obj update function and drawing function.
"""
class Scene:
    def __init__(self, listener):
        self.gameObjectList = []
        self.nextScene = None
        self.endSceneListener = listener

    def eventListener(self, event):
        """
        Handle all the functionality for relevent pygame event.
        *Need to be ovverride*
        :param event: event from the app(mouse click, button pressed etc...)
        """
        raise NotImplementedError

    def runScene(self):
        for obj in self.gameObjectList:
            obj.update()

    def drawScene(self, display_surf):
        for obj in self.gameObjectList:
            obj.draw(display_surf)

    def endScene(self):
        """
        Send back to Main app the next Scene that should be running.
        function form main that handle the "change scene" functionality.
        """
        self.endSceneListener(self.nextScene)