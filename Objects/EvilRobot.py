from Objects.Robot import Robot
import math
from GameObject.Tag import Tag

class EvilRobot(Robot):
    def __init__(self, name="EvilRobot", position=(0,0)):
        super().__init__(name, position)
        self.speed = 5
        self.reactionRate = 10
        self.fireRate = 10
        self.reactionTime = 0
        self.fireTimer = 0
        self.path = []
        self.targetIsVisible = False
        self.tag = Tag.types[2]

    def update(self, deltaTime):
        super().update(deltaTime)
        if self.reactionTime >= 0:
            self.reactionTime -= deltaTime

    def setDifficult(self, x):
        """
        Set the difficulty of the evil robot by manipulate his fireRate, reactionTime
        and speed.
        the difficulty is on the spectrum of 1 to 100.
        wen difficulty 1 is:
        speed = 5, reactionTime = 10, fireRate = 15
        and difficulty 100 is:
        speed = 10, reactionTime = 5, fireRate = 1
        :param x: difficult level
        """
        difficulty = x
        if difficulty > 100:
            difficulty = 100
        elif difficulty < 1:
            difficulty = 1
        baseSpeed = 5
        baseReaction = 10
        baseFireRtae = 20

        self.speed = baseSpeed+0.5*math.sqrt(difficulty)
        self.reactionRate = baseReaction-(math.sqrt(difficulty)-5)
        self.fireRate = baseFireRtae-(math.sqrt(difficulty)-1)
        print("setDiffcult to: {dif}, stats: speed->{s}, reaction->{r}, fireRate->{f}.".format(dif=x, s=self.speed, r=self.reactionRate, f=self.fireRate))

