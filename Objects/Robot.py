import pygame
from GameObject.GameObject import GameObject
from GameObject.Transform import Transform
from GameObject.Point import Point

class Robot(GameObject):
    def __init__(self, position):
        GameObject.__init__(self,"Robot", position)
        self.img = pygame.image.load("Resources/roboTest.png")
        self.transform.set_position(position)
        self.speed = 5
        self.walking = False
        self.nextStep = None


    def update(self):
        if(self.walking == True):
            if(self.transform.distance(point=Point((self.nextStep[0], self.nextStep[1])))>1):
                deltaTime = pygame.time.Clock().tick(30)/100
                pos = self.transform.get_position()
                if pos[0] > self.nextStep[0]:
                    self.transform.set_position((pos[0]-self.speed*deltaTime, pos[1]))
                elif pos[0] < self.nextStep[0]:
                    self.transform.set_position((pos[0]+self.speed*deltaTime, pos[1]))

                if(pos[1] > self.nextStep[1]):
                    self.transform.set_position((pos[0], pos[1]-self.speed*deltaTime))
                elif pos[1] < self.nextStep[1]:
                    self.transform.set_position((pos[0], pos[1]+self.speed*deltaTime))
            else:
                self.transform.set_position(self.nextStep)
                self.nextStep = None
                self.walking = False

    def move(self, direciton, step):
        if self.walking == False:
            self.img = pygame.transform.rotate(self.img, self._getRotate(self.transform.direction, direciton))
            self.transform.direction = direciton

        if(self.walking is False):
            self.walking = True
            pos = self.transform.get_position()
            dir = Transform.direction.get(direciton)
            self.nextStep = (pos[0]+dir[0]*step, pos[1]+dir[1]*step)
            return self.nextStep
            # print("pos: "+str(pos)+", dir: "+str(dir)+", nextStep: "+str(self.nextStep))

    def _getRotate(self, originDir, targetDir):
        dirDict = {"north": 90, "south":270, "east":0, "west":180}
        originalAngle = dirDict[originDir]
        targetAngle = dirDict[targetDir]
        angle = 0
        print("origin dir: {od}, target dir : {td}".format(od = originDir, td = targetDir))
        while (originalAngle+angle) % 360 != targetAngle:
            angle += 90
        return angle
