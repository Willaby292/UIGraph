from Graph import *
from tkinter import *
import pyautogui


class Window:
    def __init__(self, opacity=1, isFullscreen=True):
        screenWidth, screenHeight = pyautogui.size()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.opacity= opacity
        self.isFullscreen = isFullscreen

    def buildCanvas(self, POIGraph):
        root = Tk()

        geo = str(self.screenWidth)+'x'+str(self.screenHeight)
        root.geometry(geo)

        root.attributes('-fullscreen', self.isFullscreen)
        root.attributes('-alpha', self.opacity) #opacity

        w = Canvas(root, width=self.screenWidth, height=self.screenHeight)
        w.pack()

        def quit_win():
            root.destroy()

        button=Button(root,text="Quit", font=('Times New Roman', 13, 'bold'), command=quit_win)
        button.place(x=self.screenWidth/2,y=10)
        self.drawGraph(w, POIGraph)

    def drawGraph(self, w, POIGraph):
        for nodeId in POIGraph.getGraph():
            node = POIGraph.getGraph()[nodeId]
            x = node.getX()
            y = node.getY()
            w.create_oval(x - 20, y - 20, x + 20, y + 20, fill='blue', activefill='red', width=3)
            neighbors = node.getNeighbors()
            for i, n in enumerate(neighbors, 0):
                if not isinstance(n, int):
                    if i == 0:
                        w.create_line(x, y, n.getX(), n.getY(), arrow=LAST)
                    if i == 1:
                        w.create_line(x, y, n.getX(), n.getY(), arrow=LAST)
                    if i == 2:
                        w.create_line(x, y, n.getX(), n.getY(), arrow=LAST)
                    if i == 3:
                        w.create_line(x, y, n.getX(), n.getY(), arrow=LAST)

            # x_start = x
            # inverse_x_start = x

            # y_start = y
            # inverse_y_start = y
            # for dx in range(0, self.screenWidth - x, 10):
            #     dy = math.log10(dx + 1) * 100

            #     draw_line = w.create_line(x + dx, y + dy, x_start, y_start)
            #     draw_line = w.create_line(x + dx, y - dy, x_start, inverse_y_start)
            #     draw_line = w.create_line(x - dx, y + dy, inverse_x_start, y_start)
            #     draw_line = w.create_line(x - dx, y - dy, inverse_x_start, inverse_y_start)


            #     x_start = x + dx
            #     inverse_x_start = x - dx
            #     y_start = y + dy
            #     inverse_y_start = y - dy

            # x_start = x
            # inverse_x_start = x

            # y_start = y
            # inverse_y_start = y
            # for dy in range(0, self.screenHeight - y, 10):
            #     dx = math.log10(dy + 1) * 100

            #     draw_line = w.create_line(x + dx, y + dy, x_start, y_start)
            #     draw_line = w.create_line(x - dx, y + dy, inverse_x_start, y_start)
            #     draw_line = w.create_line(x + dx, y - dy, x_start, inverse_y_start)
            #     draw_line = w.create_line(x - dx, y - dy, inverse_x_start, inverse_y_start)

            #     x_start = x + dx
            #     inverse_x_start = x - dx
            #     y_start = y + dy
            #     inverse_y_start = y - dy

        mainloop()