
from Node import *
from Direction import Direction
import math
import pyautogui

def findNeighbors(currPlace, POI): #this can be never nested
    x = POI[currPlace].getX()
    y = POI[currPlace].getY()

    distOldNorthNeighbor = float('inf')
    distOldSouthNeighbor = float('inf')
    distOldEastNeighbor = float('inf')
    distOldWestNeighbor = float('inf')

    slopeC = 100 #no idea what i want this to be

    for place in POI: #TODO// handle overlapping neighbor regions
        dx = POI[place].getX() - x
        dy = POI[place].getY() - y
        if dx != 0 and dy != 0:
            if abs(dx) < math.log10(abs(dy) + 1) * slopeC:
                if dy < 0:
                    if distOldNorthNeighbor < abs(dy):
                        break
                    POI[currPlace].setNeighbor(place, Direction.UP)
                    distOldNorthNeighbor = abs(dy)
                else:
                    if distOldSouthNeighbor < dy:
                        break
                    POI[currPlace].setNeighbor(place, Direction.DOWN)
                    distOldSouthNeighbor = abs(dy)
            elif abs(dy) < math.log10(abs(dx) + 1) * slopeC:
                if dx < 0:
                    if distOldWestNeighbor < abs(dx):
                        break
                    POI[currPlace].setNeighbor(place, Direction.LEFT)
                    distOldWestNeighbor = abs(dx)
                else:
                    if distOldEastNeighbor < dx:
                        break
                    distOldEastNeighbor = dx
                    POI[currPlace].setNeighbor(place, Direction.RIGHT)

def findNeighborsHeatMap(currNodeId: int, POI):
    ## go back over list of nodes when done to check if all nodes have a least one neighbor. If not idk what to do. math might work out that its not possible?
    currNode = POI[currNodeId]
    minUp = float('inf')
    minDown = float('inf')
    minLeft = float('inf')
    minRight = float('inf')
    for nodeId in POI:
        if nodeId == currNodeId:
            continue
        node = POI[nodeId]
        dx = node.getX() - currNode.getX()
        dy = node.getY() - currNode.getY()
        matchVal = abs(dx) + abs(dy)
        if dy <= dx and dy <= -dx: #up down math flipped bc computer science knows better than math i guess...
            if matchVal < minUp:
                currNode.setNeighbor(node, Direction.UP)
                minUp = matchVal
        elif dy >= dx and dy >= -dx:
            if matchVal < minDown:
                currNode.setNeighbor(node, Direction.DOWN)
                minDown = matchVal
        elif dy >= dx and dy <= -dx:
            if matchVal < minLeft:
                currNode.setNeighbor(node, Direction.LEFT)
                minLeft = matchVal
        elif dy <= dx and dy >= -dx:
            if matchVal < minRight:
                currNode.setNeighbor(node, Direction.RIGHT)
                minRight = matchVal


def buildGraph(POI):
    for place in POI:
        findNeighborsHeatMap(place, POI)
    return POI

def createNodePOI(POI) -> dict:
    nodePOI = {}
    for count, node in enumerate(POI):
        nodePOI[count] = Node(node[0], node[1])
    return nodePOI

class Graph:
    def __init__(self, POI: list):
        nodePOI = createNodePOI(POI)
        self.graph = buildGraph(nodePOI)
        self.currNode = self.graph[0]


    def getGraph(self):
        return self.graph

    def moveMouse(self, direction):
        node = self.currNode.getNeighbors(direction)
        if not node == -1:
            x = node.getX()
            y = node.getY()
            pyautogui.moveTo(x, y)
            self.currNode = node