from collections import defaultdict
from enum import IntEnum

obstaclesRow = defaultdict(lambda: [])
obstaclesCol = defaultdict(lambda: [])

gridSize = (0,0)

class Direction(IntEnum):
    UP    = 0
    RIGHT = 1
    DOWN  = 2
    LEFT  = 3

def between(n,a,b):
    if min(a,b) <= n <= max(a,b):
        return True
    return False

def nextPoint(point,dir):
    global obstaclesRow
    global obstaclesCol
    global gridSize

    if min(point) < 0 or point[0] >= gridSize[0] or point[1] >= gridSize[1]:
        return None

    try:
        if dir == Direction.UP:
            x = point[1]
            y = max([Y for Y in obstaclesCol[x] if Y < point[0]])
            return (y+1,x+0)
        if dir == Direction.DOWN:
            x = point[1]
            y = min([Y for Y in obstaclesCol[x] if Y > point[0]])
            return (y-1,x+0)
        if dir == Direction.LEFT:
            y = point[0]
            x = max([X for X in obstaclesRow[y] if X < point[1]])
            return (y+0,x+1)
        if dir == Direction.RIGHT:
            y = point[0]
            x = min([X for X in obstaclesRow[y] if X > point[1]])
            return (y+0,x-1)
    except ValueError:
        if dir == Direction.UP:
            return (-1,x)
        if dir == Direction.DOWN:
            return (gridSize[0],x)
        if dir == Direction.LEFT:
            return (y,gridSize[1])
        if dir == Direction.RIGHT:
            return (y,-1)
        
def pathTravelled(path):
    lines = []
    for first, second in zip(path, path[1:]):
        lines.append( (first,second) )

    fullPath = []
    for l in lines:
        l = sorted(l)
        if l[0][0] == l[1][0]:
            for x in range(l[0][1],l[1][1]+1):
                fullPath.append( (l[0][0],x) )
        if l[0][1] == l[1][1]:
            for y in range(l[0][0],l[1][0]+1):
                fullPath.append( (y,l[0][1]) )

    return len(set(fullPath)) - 1
    



def Part1(data):
    global obstaclesRow
    global obstaclesCol
    global gridSize
    gridSize = (len(data),len(data[0]))

    start = (-1,-1)
    dir   = Direction.UP

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                obstaclesRow[y].append(x)
                obstaclesCol[x].append(y)
            if data[y][x] == '^':
                start = (y,x)

    Path = [start]
    while point:=nextPoint(Path[-1],dir):
        Path.append(point)
        dir = Direction( (dir+1)%4 )
    return pathTravelled(Path)

def Part2(data):
    global obstaclesRow
    global obstaclesCol
    global gridSize

    start = (-1,-1)
    dir   = Direction.UP

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '^':
                start = (y,x)

    loops = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                continue
            else:
                obstaclesRow[y].append(x)
                obstaclesCol[x].append(y)

            oldConfig = set()

            Path = [start]
            dir   = Direction.UP
            while (point:=nextPoint(Path[-1],dir)) and (Path[-1],dir) not in oldConfig:
                oldConfig.add( (Path[-1],dir) )
                Path.append(point)
                dir = Direction( (dir+1)%4 )
            if (Path[-1],dir) in oldConfig:
                loops += 1
            
            obstaclesRow[y].remove(x)
            obstaclesCol[x].remove(y)
    return loops