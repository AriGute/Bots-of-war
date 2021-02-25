"""
Scene represent some kind of game state(for exemple: main menu, gameMode etc...).
Wen the Main loop is focusing on some scene then for each element in the gameObj list
the main loop should run the obj update function and drawing function.
"""
class Scene:
    def __init__(self, listener):
        self._gameObjectList = {}
        self.nextScene = None
        self.endSceneListener = listener

    def eventListener(self, event):
        """
        Handle all the functionality for relevent pygame event.
        *Need to be override*
        :param event: event from the app(mouse click, button pressed etc...)
        """
        raise NotImplementedError

    def runScene(self):
        """
        Every frame call the update method of every gameObject of this Scene.
        """
        for obj in self._gameObjectList.values():
            obj.update()

    def drawScene(self, display_surf):
        """
        Every frame call the draw method of every gameObject of this Scene.
        """
        for obj in self._gameObjectList.values():
            obj.draw(display_surf)

    def endScene(self):
        """
        Send back to Main app the next Scene that should be running.
        function form main that handle the "change scene" functionality.
        """
        self.endSceneListener(self.nextScene)

    def addGamObj(self, k, obj):
        """
        Add new key and value(gameObject) to dictionary(gameObjList)
        :param k: represented item name
        :param obj: the game obj that need to be stored
        """
        key = k
        while key in self._gameObjectList.keys():
            # if there is alredy existing key
            splitKey = str(key).split(" ")
            if splitKey[-1].isdigit():
                # if the key have digit in the and after space(someKey 1)
                # then add +1 to the digit at the end
                for i in range(0, len(splitKey)-1):
                    key += splitKey[i] + " "
                key += str(int(splitKey[-1])+1)
            else:
                # if the key don't have any digit at the end then add one to make the key unique.
                key += " 1"
        self._gameObjectList[key] = obj

    def getGameObj(self, k):
        """
        :param k: gameObject name as key
        :return: gameObject from the gameObjectList of the Scene
        """
        return self._gameObjectList.get(k)

    def drawTiledMap(self, display_surf):
        pass