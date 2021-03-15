import pygame
from Scenes.Scene import Scene
from Objects.Robot import Robot
from Objects.EvilRobot import EvilRobot
from GameObject.Transform import Transform
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from GameObject.Point import Point
from math import trunc
import pdb

# TODO: create function that clear the memory properly.
class GameScene(Scene):

    def __init__(self, nextSceneListener, difficulty=1, level=1):
        """
        :param difficulty: the difficulty(1,..., 100) of the EvilRobot.
        :param level: the wanted level(tiledMap and spawnPoints).
        """
        Scene.__init__(self, nextSceneListener)
        self.step = 50
        self.w, h = pygame.display.get_surface().get_size()
        self.display_surf = None
        self.Resources.append(pygame.image.load("Resources/ground_mud.png"))
        self.Resources.append(pygame.image.load("Resources/wall.png"))

        level = self.getLevel(level)
        spawnPoint = level[1]
        self.tiledMap = level[0]

        self.addGamObj("Robot", Robot("Robot", spawnPoint[0]))
        self.addGamObj("EvilRobot", EvilRobot("EvilRobot", spawnPoint[1]))

        self.player = self.getGameObj("Robot")
        self.evilRobot = self.getGameObj("EvilRobot")
        self.evilRobot.setDifficult(difficulty)




    def eventListener(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # targetPos = self.player.transform.get_gridPosition()
            # targetPos = targetPos
            # print(targetPos)
            # mousePos = (trunc(pygame.mouse.get_pos()[0]/50), trunc(pygame.mouse.get_pos()[1]/50))
            # print(mousePos)
            # print()
            # print(self.rayCast2(mousePos, targetPos))
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
        pass

    def evilRoborAi(self):
        """
        EvilRobot Ai.
        calc the EvilRobot next move
        or fire action.
        """
        # if Evil robot shoot after moving then its create a bug that
        # make the Projectile be over a Robot(tiledMap[][] == 2)
        # and destroying the Projectile.
        # Fixed the bug by add some fix time after each shot
        # to reactionTime and make the EvilRobot wait before he
        # move again(and walk over hes own Projectile).
        if self.evilRobot.fireTimer <= 0:
            # Evil robot try to shoot.
            targetPos = self.player.transform.get_gridPosition()
            myGridPos = self.evilRobot.transform.get_gridPosition()

            rayCastHit = self.rayCast(myGridPos, targetPos)
            for hit in rayCastHit:
                objType = rayCastHit[hit]
                if objType == 1:
                    break
                elif objType == 2:
                    if self.isInfront(myGridPos,
                                      Transform.direction[self.evilRobot.transform.direction], 2):
                        Projectile = self.evilRobot.fire()
                        if Projectile is not None:
                            self.addGamObj("Projectile", Projectile)
                            Projectile.move(self.evilRobot.transform.direction)
                            # Add some time to reaction time and make the
                            # robot wait after each shot before walk(over his own projectile).
                            self.evilRobot.reactionTime += self.evilRobot.fireRate/2
                        else:
                            self.evilRobot.fireTimer = self.evilRobot.fireRate

        if self.evilRobot.reactionTime <= 0:
            # Evil robot try to move.
            targetPos = self.player.transform.get_position()
            if self.evilRobot.transform.distance(Point(targetPos)) > self.step:
                startPos = self.getGameObj("EvilRobot").transform.get_gridPosition()
                targetPos = self.getGameObj("Robot").transform.get_gridPosition()
                self.evilRobot.reactionTime = self.evilRobot.reactionRate
                nextDirection = self.pathFinding(startPos, targetPos)
                if nextDirection is not None:
                    self.evilRobot.move(nextDirection)





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
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
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
        if len(path) > 0:
            direction = (path[1][0] - self.evilRobot.transform.get_gridPosition()[0],
                         path[1][1] - self.evilRobot.transform.get_gridPosition()[1])
        else:
            return None
        # convert next step to direction('north', 'south', etc..).
        inv_map = {v: k for k, v in Transform.direction.items()}

        # return next step direction as string.
        return inv_map[direction]

    def getLevel(self, level):
        """
        This function hold dictionary of levels and spawn points for each
        level.
        :param level: the key as number of the wanted level.
        :return: the wanted level as list of [level, spawnPoints]
        """
        levels = {0: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

                  1: [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
                      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

                  2: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        }

        spawnPoints = {0: [(5, 5), (0, 1)],
                       1: [(3, 10), (4, 1)],
                       2: [(1, 10), (13, 1)]
        }

        Spawn = spawnPoints[level]
        scaledSpawn = [(Spawn[0][0]*self.step, Spawn[0][1]*self.step),
                       (Spawn[1][0]*self.step, Spawn[1][1]*self.step)]

        return [levels[level], scaledSpawn]

    def isInfront(self, pos, dir, tag):
        """
        Check if tiledMap[][]==tag on the line from the position
        and in the direction from the position.
        :param pos: start position.
        :param dir: direction to check from the start position(as tuple).
        :param tag: the gameObject we are looking for.
        :return: True if the Tag exist on the line or False if not.
        """
        cell = None
        nextPos = pos
        nextPos = (nextPos[0] + dir[0], nextPos[1] + dir[1])
        x, y = 0, 0
        while True:
            nextPos = (nextPos[0]+dir[0], nextPos[1]+dir[1])
            x = nextPos[0]
            y = nextPos[1]
            if x < 0 or x >= len(self.tiledMap[0])or y < 0 or y >= len(self.tiledMap):
                return False
            else:
                cell = self.tiledMap[y][x]
                if cell == tag:
                    return True
                elif cell == 0:
                    continue
                else:
                    return False


    def rayCast(self, pos1, pos2):

        container = {}
        p1 = (pos1[1], pos1[0])
        p2 = (pos2[1], pos2[0])


        x1 = p1[1]
        y1 = p1[0]
        x2 = p2[1]
        y2 = p2[0]

        x, y = x1, y1
        m = ((y1-y2)/(x1-x2) if (x1-x2) != 0 else 0)
        lineX = lambda x: m*(x-x2)+y2
        lineY = lambda y: (((y-y2)/m)+x2) if (m != 0) else (0 + x2)

        while x <= len(self.tiledMap[0]) if x1 < x2 else x >= 0:
            y = lineX(x)
            y = trunc(y)
            if y > len(self.tiledMap)-1 or x > len(self.tiledMap[0])-1 or x < 0 or y < 0:
                break
            container[(y,x)] = self.tiledMap[y][x]
            if p1[1] < p2[1]:
                x = x + 1
            else:
                x = x-1

        x = x1
        y = y1
        while y <= len(self.tiledMap) if y1 < y2 else y >= 0:
            x = lineY(y)
            x = abs(trunc(x))
            if y > len(self.tiledMap)-1 or x > len(self.tiledMap[0])-1 or x < 0 or y < 0:
                break
            container[(y, x)] = self.tiledMap[y][x]

            if p1[0] < p2[0]:
                y = y + 1
            else:
                y = y - 1
        # pdb.set_trace()
        # for cell in container.keys():
        #     if self.tiledMap[cell[0]][cell[1]] == 2:
        #         print("found it!")
        #         break
        container.pop((pos1[1], pos1[0]))
        return container