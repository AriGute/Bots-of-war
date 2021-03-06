import pygame
from Scenes.Scene import Scene
from Objects.Robot import Robot
from Objects.EvilRobot import EvilRobot
from GameObject.Transform import Transform
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from GameObject.Point import Point

# TODO: investigate bug that happen if EvilRobot walk near
#  eadge of the screen then he stop moving.
# TODO: create function that clear the memory properly.
class GameScene(Scene):

    def __init__(self, nextSceneListener):
        Scene.__init__(self, nextSceneListener)
        self.step = 50;
        self.w, h = pygame.display.get_surface().get_size()
        self.display_surf = None
        self.Resources.append(pygame.image.load("Resources/ground_mud.png"))
        self.Resources.append(pygame.image.load("Resources/wall.png"))
        self.tiledMap = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.addGamObj("Robot", Robot((50, 500)))
        self.addGamObj("EvilRobot", EvilRobot((50, 0)))

        self.player = self.getGameObj("Robot")
        self.evilRobot = self.getGameObj("EvilRobot")

    def eventListener(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
           for i in self.takeSnapShot():
               print(i)
           print("\n")

        if event.type == pygame.KEYDOWN:
            if self.player.Moving != True:
                robot = self.player
                robotNextPos = None
                Projectile = None
                direction = None
                if event.key == pygame.K_LEFT:
                    direction = 'west'
                elif event.key == pygame.K_RIGHT:
                    direction = 'east'
                elif event.key == pygame.K_UP:
                    direction = 'north'
                elif event.key == pygame.K_DOWN:
                    direction = 'south'
                elif event.key == pygame.K_SPACE:
                    Projectile = robot.fire()
                    if Projectile is not None:
                        self.addGamObj("Projectile", Projectile)
                        Projectile.move(robot.transform.direction)

                if direction is not None:
                    nextPos = self.player.transform.calcNextPos(direction)
                    if self.cellIsWalkAble(nextPos[0], nextPos[1]):
                        if self.player.transform.inBounds(nextPos):
                            robot.move(direction)


    def update(self, deltaTime):
        self.evilRoborAi()

    def evilRoborAi(self):
        """
        EvilRobot Ai.
        calc the EvilRobot next move
        or fire action.
        """
        # if Evil robot shoot after moving then its create a bug that
        # make the Projectile think that its over a Robot(tiledMap[][] == 2)
        # and destroying the Projectile.
        if self.evilRobot.fireTimer <= 0:
            # Evil robot try to shoot.
            targetPos = self.player.transform.get_gridPosition()
            myGridPos = self.evilRobot.transform.get_gridPosition()
            if targetPos[0] == myGridPos[0] or targetPos[1] == myGridPos[1]:
                Projectile = self.evilRobot.fire()
                if Projectile is not None:
                    self.addGamObj("Projectile", Projectile)
                    Projectile.move(self.evilRobot.transform.direction)
        if self.evilRobot.reactionTime <= 0:
            # Evil robot try to move.
            targetPos = self.player.transform.get_position()
            if self.evilRobot.transform.distance(Point(targetPos)) > self.step:
                startPos = self.getGameObj("EvilRobot").transform.get_gridPosition()
                targetPos = self.getGameObj("Robot").transform.get_gridPosition()
                self.evilRobot.reactionTime = self.evilRobot.reactionRate
                self.evilRobot.move(self.pathFinding(startPos, targetPos))



    def pathFinding(self, start, target):
        """
        Using A* path finding to get the direction of the next step
        on the path from the start position to the target position.

        The start and target position need to ve converted to
        the form (int, int) to fit in the matrix/tiledMap.

        :param start: start position(int, int) as tuple.
        :param target: end position(int, int) as tuple.
        :return: direction of the next step on the grid as string.
        """

        matrix = []
        # make a copy of the tiledMap.
        for i in range(len(self.tiledMap)):
            matrix.append(self.tiledMap[i].copy())

        # change the tiledmap to 1(walkable) and 0(obstacle).
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                elif matrix[i][j] == 2:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0

        grid = Grid(matrix=matrix)

        # set start point and end point on the grid.
        start = grid.node(start[0], start[1])
        end = grid.node(target[0], target[1])

        # run A* algorithm from start node to end node on the grid.
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)

        # get the next move in the path as touple of direction(one step to any side)
        direction = (path[1][0] - self.evilRobot.transform.get_gridPosition()[0],
                     path[1][1] - self.evilRobot.transform.get_gridPosition()[1])

        # convert next step to direction('north', 'south', etc..).
        inv_map = {v: k for k, v in Transform.direction.items()}

        # return next step direction as string.
        return inv_map[direction]
