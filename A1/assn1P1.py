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
        self.setWindowTitle('CMPT310 Assn1P1')
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
            elif point in route[endpt]:
                col = QColor(0,0,0)
            else:
                col = QColor(160,160,160)
            painter.setBrush(col)
            painter.drawRect(30*point[0],-(30*point[1]-510),29,29)

# the heuristic function, which return the Cartesian distance between 2 points
def heuristic(coor):
    hlen = abs(coor[0]-endx) + abs(coor[1]-endy)
    return hlen

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

# initialize the route, which store the route 
# towards each point
route = dict()
for x in range(18):
    for y in range(18):
        route[(x,y)] = list()

# initialize the frontier heap with start point
# the "frnt" list stores all points that used to 
# be frontier, which could avoid adding the same 
# point into frontier heap one more time
frontier = list()
frnt = list()
frontcnt = -1
frontier.append((heuristic(startpt),startpt))
frnt.append(startpt)
is_end = 1

# until the end point has been found, pop the point of smallest heuristic
# distance. and add its adjacent points into frontier
while is_end:
    frontcnt += len(frontier)
    newpt = heappop(frontier)
    newpt = newpt[1]
    for fronpt in coordinate[newpt]:
        if fronpt == endpt:
            route[fronpt] = route[newpt]
            route[fronpt].append(newpt)
            route[fronpt].append(endpt)
            is_end = 0
            break
        elif fronpt not in frnt:
            frnt.append(fronpt)
            for pt in route[newpt]:
                route[fronpt].append(pt)
            route[fronpt].append(newpt)
            heappush(frontier,(heuristic(fronpt),fronpt))

print("the total cost is ", len(route[endpt])-1)
print("the total number of frontier is ",frontcnt)
print("the route is ", route[endpt])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = Interface()
    sys.exit(app.exec_())

