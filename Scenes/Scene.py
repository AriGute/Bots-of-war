from math import trunc
from GameObject.Tag import Tag

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

        self.size = self.weight, self.height = 800, 600

    def eventListener(self, event):
        """
        Handle all the functionality for relevent pygame event.
        *Need to be override*
        :param event: event from the app(mouse click, button pressed etc...)
        """
        raise NotImplementedError

    def runScene(self, deltaTime):
        """
        Every frame call the update method of every gameObject of this Scene.
        """
        self.update(deltaTime)
        for obj in self._gameObjectList.copy().values():
            obj.update(deltaTime)
            self.redraw(obj.transform.get_position())

    def update(self, deltaTime):
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
            # print(splitKey[-1])
            if splitKey[-1].isdigit():
                # if the key have digit in the and after space(someKey 1)
                # then add +1 to the digit at the end
                # TODO: change 'name 1' to 'name 1name 1' instead of 'name 2'(need to be fixed!).
                key = splitKey[0]+" "+str(int(splitKey[1])+1)
                print(key)
                # for i in range(0, len(splitKey)-1):
                #     key += splitKey[i] + " "
                # key += str(int(splitKey[-1])+1)
            else:
                # if the key don't have any digit at the end then add one to make the key unique.
                key += " 1"
        obj.addFunctionRef('rePos', self.rePosObj)
        obj.name = key
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
            for pos in [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]:
                if pos[1] < len(self.tiledMap) and pos[0] < len(self.tiledMap[0]):
                    if self.tiledMap[pos[1]][pos[0]] > 0:
                        if self.tiledMap[pos[1]][pos[0]] < len(self.Resources):
                            self.display_surf.blit(self.Resources[self.tiledMap[pos[1]][pos[0]]], (self.step * pos[0], self.step * pos[1]))
                        else:
                            self.display_surf.blit(self.Resources[0], (self.step * pos[0], self.step * pos[1]))
                    else:
                        self.display_surf.blit(self.Resources[0], (self.step * pos[0], self.step * pos[1]))

    def takeSnapShot(self):
        """
        This function generate dataset for later usage for the AI module.
        dataset contain the features:
            Tiled map: position of everything.
            Player robot health.
            Player fireTime: if fireTime is 0 then the Player can shoot again.
            Player robot direction: direction translated to 1,..,4(one for each direction).
            EvilRobot health.
            EvilRobot fireTime: if fireTime is 0 then the EvilRobot can shoot again.
            EvilRobot direction: translated to 1,..,4 one for each direction.
            If evilRobot currently know where is the player robot(0 or 1).
        :return: snapshot of the state of the game as list.
        """
        snapshot = [self.tiledMap]
        player = self.getGameObj("Robot")
        evilRobot = self.getGameObj("EvilRobot")
        dir = {
            "west": 1,
            "east": 2,
            "south": 3,
            "north": 4,
        }

        snapshot.append(player.health)
        snapshot.append(int(player.fireTimer))
        snapshot.append(dir[player.transform.direction])
        snapshot.append(evilRobot.health)
        snapshot.append(int(evilRobot.fireTimer))
        snapshot.append(dir[evilRobot.transform.direction])
        snapshot.append(1 if evilRobot.targetIsVisible else 0)

        # prints for debuging.
        print()
        for i in snapshot[0]:
            print(i, end="\n")
        for i in snapshot[1:]:
            print(i)

        return snapshot

    def nextScene(self, scene):
        self.endSceneListener(scene)

    def rePosObj(self, oldPos, newPos, id, tag, name):
        if newPos is not None and oldPos is not None:
            x1 = trunc(newPos[0] / self.step)
            y1 = trunc(newPos[1] / self.step)
            x2 = trunc(oldPos[0] / self.step)
            y2 = trunc(oldPos[1] / self.step)

            if x1 < 0 or x1 >= self.weight/self.step or y1 < 0 or y1 >= self.height/self.step:
                key = self.getObjKey(id)
                self.removeObj(key, x2, y2)
                return
            if self.tiledMap[y1][x1] == 1:
                key = self.getObjKey(id)
                # pdb.set_trace()
                self.removeObj(key, x2, y2)
                return


            type = 0
            if tag == Tag.types[1]:
                '''type = Player'''
                type = 2
            if tag == Tag.types[2]:
                '''type = EvilRobot'''
                type = 2
            elif tag == Tag.types[3]:
                '''type = Projectile'''
                # if Projectile spawned out of Robot then don't override the Robot from the tiledmap.
                if self.tiledMap[y1][x1] == 2:
                    projectile = self.getGameObj(name)
                    if projectile.source == Tag.types[1]:
                        '''type = Player'''
                        self.getGameObj("EvilRobot").health -= projectile.damage
                        # print("EvilRobot health: "+str(self.getGameObj("EvilRobot").health))
                    if projectile.source == Tag.types[2]:
                        '''type = EvilRobot'''
                        self.getGameObj("Robot").health -= projectile.damage
                        # print("Player health: "+str(self.getGameObj("Robot").health))

                    key = self.getObjKey(id)
                    # pdb.set_trace()
                    self.removeObj(key, x2, y2)
                    return
                else:
                    type = -1

            self.tiledMap[y1][x1] = type
            self.tiledMap[y2][x2] = 0

    def cellIsWalkAble(self, x, y):
        """
        Check if cell on the tiledmap is walkable(0 mean no obstacle).
        :param x: number of pixels on the x axis
        :param y:number of pixels on the y axis
        :return: True if the cell is walkable(0 in the tiled map)
        """
        i = trunc(y/self.step)
        j = trunc(x/self.step)
        if j < 0 or j >= self.weight / self.step or i < 0 or i >= self.height / self.step:
            return False
        if self.tiledMap[i][j] == 0:
            return True
        return False

    def getObjKey(self, id):
        """
        Return the key for the giving object id.
        gameObjectList with this key will give object with the same id.
        if cant find any gameObject with same id then return None.
        :param id: existing gameObjct id.
        :return: dictionary key for that gameObject.
        """
        for i in range(len(self._gameObjectList)):
            key = list(self._gameObjectList.keys())[i]
            if self.getGameObj(key).id == id:
                return key
        return None

    def removeObj(self, key, x, y):
        """
        Remove gameObject from gameObjectList dictionary and remove it from the tiledmap.
        :param key: game object key in the gameObjList.
        :param x: row index in the tiledmap.
        :param y: column index in th etiledmap.
        """
        self._gameObjectList.pop(key)
        self.tiledMap[y][x] = 0

    def printMap(self):
        """
        For debugging.
        print tiled map and all objects that
        are currently in the scene.
        """
        print()
        for i in self._gameObjectList.values():
            print(i)
        print()
        for i in self.tiledMap:
            print(i)


