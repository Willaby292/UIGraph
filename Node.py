from Direction import *


# 0(800, 350) 1(950, 350) 2(1100, 350)
# 3(800, 500) 4(950, 500) 5(1100, 500)
# 6(800, 650) 7(950, 650) 8(1100, 650)


# x range 800-1100 = 300 intervals of 150
# y range 350-650 = 300  intervals of 150


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = [-1, -1, -1, -1] #up, down, left, right

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNeighbors(self, direction=None):
        if direction == None:
            return self.neighbors
        if not isinstance(direction, Direction):
            raise ValueError('direction argument must be instance of Direction enum')
        return self.neighbors[direction.value]

    def setNeighbor(self, neighbor, direction):
        self.neighbors[direction.value] = neighbor