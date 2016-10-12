# initialize the coordinate according to the assignment requirements

coordinate = dict()
for x in range(18):
    for y in range(18):
        if x == 7 and y <= 9 and y >= 5:
            pass
        elif x <= 15 and x >= 10 and y == 13:
            pass
        elif x == 15 and y == 12:
            pass
        else:
            coordinate[(x, y)] = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]

for x in range(18):
    coordinate[(x, 0)].remove((x, -1))
    coordinate[(x, 17)].remove((x, 18))

for y in range(18):
    coordinate[(0, y)].remove((-1, y))
    coordinate[(17, y)].remove((18, y))

for y in range(5, 10):
    coordinate[(6, y)].remove((7, y))
    coordinate[(8, y)].remove((7, y))

for x in range(10, 15):
    coordinate[(x, 12)].remove((x, 13))
    coordinate[(x, 14)].remove((x, 13))

coordinate[(7, 4)].remove((7, 5))
coordinate[(7, 10)].remove((7, 9))
coordinate[(9, 13)].remove((10, 13))
coordinate[(15, 14)].remove((15, 13))
coordinate[(16, 13)].remove((15, 13))
coordinate[(16, 12)].remove((15, 12))
coordinate[(15, 11)].remove((15, 12))
coordinate[(14, 12)].remove((15, 12))

# mark the landmarks
landmarks = list()
landmarks.append((7,5))
landmarks.append((7,6))
landmarks.append((7,7))
landmarks.append((7,8))
landmarks.append((7,9))
landmarks.append((10,13))
landmarks.append((11,13))
landmarks.append((12,13))
landmarks.append((13,13))
landmarks.append((14,13))
landmarks.append((15,13))
landmarks.append((15,12))
