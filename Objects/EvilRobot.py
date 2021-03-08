from Objects.Robot import Robot

class EvilRobot(Robot):
    def __init__(self, name = "EvilRobot", position=(0,0)):
        super().__init__(name, position)
        self.speed = 5
        self.reactionRate = 10
        self.fireRate = 10
        self.reactionTime = 0
        self.fireTimer = 0

    def update(self, deltaTime):
        super().update(deltaTime)
        if self.reactionTime >= 0:
            self.reactionTime -= deltaTime
