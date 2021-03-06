from Objects.Robot import Robot

class EvilRobot(Robot):
    def __init__(self, position):
        super().__init__(position)
        self.speed = 5
        self.reactionRate = 10
        self.fireRate = 10
        self.reactionTime = 0
        self.fireTimer = 0

    def update(self, deltaTime):
        super().update(deltaTime)
        if self.reactionTime > 0:
            self.reactionTime -= deltaTime
