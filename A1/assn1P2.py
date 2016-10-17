#!python3.5
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from map import *
from heapq import *
import sys


class Interface(QWidget):
    # initialize the instance and set the windows size, title,
    # and make it visible
    def __init__(self):
        super().__init__()
        self.resize(540,540)
        self.setWindowTitle('CMPT310 Assn1P2')
        self.show()
    # override the paintEvent function and draw rectangulars filled
    # with different color
    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        self.drawR(painter)
        painter.end()
    # set the backfound color to make the frame invisible
    # draw rectangular filled with different color, which
    # depends on the point position
    def drawR(self,painter):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        painter.setPen(col)

        for point in coordinate.keys():
            if point == startpt:
                col = QColor(255, 0, 0)
            elif point == endpt:
                col = QColor(0, 0, 255)
            elif point in intrpt:
                col = QColor(0, 255, 0)
            elif point in route1[0]:
                col = QColor(0,0,0)
            elif point in route2[0]:
                col = QColor(0,0,0)
            else:
                col = QColor(160,160,160)
            painter.setBrush(col)
            painter.drawRect(30*point[0],-(30*point[1]-510),29,29)

# the heuristic function, which return the Cartesian distance between given
# point and the nearest lanmark
def heuristic(coor):
    hlen = list()
    hlen.append(abs(coor[0]-5) + abs(coor[1]-12))
    hlen.append(abs(coor[0]-12) + abs(coor[1]-12))
    hlen.append(abs(coor[0]-5) + abs(coor[1]-5))
    hlen.append(abs(coor[0]-12) + abs(coor[1]-5))
    return min(hlen)

# until the nearest landmark has been found, pop the point of smallest evaluation
# function, which is the sum of heuristic distance and the current route length,
# and add its adjacent points into frontier
def findintrpt(startpt):
    route = dict()
    for x in range(18):
        for y in range(18):
            route[(x,y)] = list()

    frontier = list()
    frnt = list()
    frontcnt = -1
    frontier.append((len(route[startpt])+heuristic(startpt),startpt))
    frnt.append(startpt)

    while 1:
        frontcnt += len(frontier)
        newpt = heappop(frontier)
        newpt = newpt[1]
        for fronpt in coordinate[newpt]:
            if fronpt in intrpt:
                route[fronpt] = route[newpt]
                route[fronpt].append(newpt)
                route[fronpt].append(fronpt)
                return route[fronpt],fronpt,frontcnt
            elif fronpt not in frnt:
                frnt.append(fronpt)
                for pt in route[newpt]:
                    route[fronpt].append(pt)
                route[fronpt].append(newpt)
                heappush(frontier,(len(route[fronpt])+heuristic(fronpt),fronpt))

# initialize the list of landmarks
intrpt = list()
intrpt.append((5,12))
intrpt.append((12,12))
intrpt.append((5,5))
intrpt.append((12,5))

# get the position of start point and end point
stax = int(input("the x-axis of start point: "))
stay = int(input("the y-axis of start point: "))
endx = int(input("the x-axis of end point: "))
endy = int(input("the y-axis of end point: "))
startpt = (stax,stay)
endpt = (endx,endy)
if startpt in landmarks or endpt in landmarks:
    print("the point is illegal")
    sys.exit()
    
# get the routes from given point to nearest landmark
route1 = findintrpt(startpt)
route2 = findintrpt(endpt)

# if landmarks are C and D, the shortest path between
# landmarks will be 9, otherwise, it will be the Cartesian
# distance between these 2 landmarks
if {route1[1],route2[1]} == {(5,5),(12,5)}:
    disintr = 9
else:
    disintr = abs(route1[1][0]-route2[1][0]) + abs(route1[1][1]-route2[1][1])

print("the total cost is ", len(route1[0])+len(route2[0])+disintr-2)
print("the total number of frontier is ",route1[2]+route2[2])
print("the route is ", route1[0]+route2[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = Interface()
    sys.exit(app.exec_())

