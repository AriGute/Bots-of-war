from math import trunc

"""
Scene represent some kind of game state(for exemple: main menu, gameMode etc...).
Wen the Main loop is focusing on some scene then for each element in the gameObj list
the main loop should run the obj update function and drawing function.
"""
class Scene:
    def __init__(self, nextSceneListener):
        self._gameObjectList = {}
        self.endSceneListener = nextSceneListener
        self.display_surf = None
        # Resources hold all the tiled map img or any other need to be "fast loaded" img.
        self.Resources = []
        # step is the number of pixels per cell in the tiled map.
        self.step = None
        # tiledMpa is a matrix n on m that each matrix cell represent pixels group(img with size step x step).
        self.tiledMap = None

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
        self.update()
        for obj in self._gameObjectList.values():
            obj.update()
            self.redraw(obj.transform.get_position())

    def update(self):
        raise NotImplementedError

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
        """
        Draw Tilled map on the display surface once.
        """
        if self.tiledMap is not None:
            self.display_surf = display_surf
            for j in range(0, len(self.tiledMap)):
                for i in range(0, len(self.tiledMap[0])):
                    display_surf.blit(self.Resources[self.tiledMap[j][i]], (self.step * i, self.step * j))

    def redraw(self, objPos):
        """
        Used if gameObject from the Scene is gonna change position.
        Redraw override the last tiled map cells the gameObject was over in his previous position.
        :param objPos:
        :return:
        """
        if self.tiledMap is not None:
            x = trunc(objPos[0] / self.step)
            y = trunc(objPos[1] / self.step)
            # self.tiledMap[y][x] = 0
            for pos in [(x,y), (x+1,y), (x,y+1), (x+1,y+1)]:
                if pos[1] < len(self.tiledMap) and pos[0] < len(self.tiledMap[0]):
                    if self.tiledMap[pos[1]][pos[0]] < len(self.Resources):
                        self.display_surf.blit(self.Resources[self.tiledMap[pos[1]][pos[0]]], (self.step * pos[0], self.step * pos[1]))
                    else:
                        self.display_surf.blit(self.Resources[0], (self.step * pos[0], self.step * pos[1]))


    def takeSnapShot(self):
        snapshot = self.tiledMap
        return snapshot

    def nextScene(self, scene):
        self.endSceneListener(scene)
