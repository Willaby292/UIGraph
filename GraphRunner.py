from Graph import *
from Window import *
import pyautogui
import random
import keyboard
from tkinter import *
import time

screenWidth, screenHeight = pyautogui.size()

def create_random_poi(screenWidth=screenWidth, screenHeight=screenHeight, num_dicts=random.randint(15, 30)):
    POI = []
    for i in range(num_dicts):
        POI.append({
            'name': i,
            'x': random.randint(20, screenWidth-20),
            'y': random.randint(20, screenHeight-20)
        })
    return POI

def recordClicks():
    print('recording...')
    print('press X to add a new point of interest on current mouse position')
    print('press - to stop recording')
    listOfClicks = []
    while True:
        event = keyboard.read_event()
        if event.name == 'x':
            x, y = pyautogui.position()
            tuple = (x, y)
            listOfClicks.append(tuple)
        elif event.name == '-':
            break
        # elif event == 't': impliment user giving list of x y coords
        #     input = ''
        #     break
        time.sleep(0.5)
    return listOfClicks

# random_poi = create_random_poi()
userPOI = recordClicks()

POIGraph = Graph(userPOI)

keyboard.add_hotkey('up', POIGraph.moveMouse, args=(Direction.UP,))
keyboard.add_hotkey('down', POIGraph.moveMouse, args=(Direction.DOWN,))
keyboard.add_hotkey('left', POIGraph.moveMouse, args=(Direction.LEFT,))
keyboard.add_hotkey('right', POIGraph.moveMouse, args=(Direction.RIGHT,))

window = Window(opacity=0.4)
window.buildCanvas(POIGraph)
