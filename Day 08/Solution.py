from collections import defaultdict
from itertools import combinations

def inBounds(point,gridSize):
    for p,g in zip(point,gridSize):
        if not (0 <= p < g):
            return False
    return True

def antiNodesP1(antennas,gridSize):
    addVec = lambda v1,v2: tuple(map(lambda a,b: a+b,v1,v2))
    subVec = lambda v1,v2: tuple(map(lambda a,b: a-b,v1,v2))

    antiNodePositions = set()
    for v1,v2 in combinations(antennas,2):
        dir = subVec(v2,v1)
        # v_2 + (v_2-v_1) and v_1 - (v_2-v_1) 
        antiNodePositions.add( addVec(v2,dir) )
        antiNodePositions.add( subVec(v1,dir) )
    return {antiNode for antiNode in antiNodePositions if inBounds(antiNode,gridSize)}

def antiNodesP2(antennas,gridSize):
    addVec = lambda v1,v2: tuple(map(lambda a,b: a+b,v1,v2))
    subVec = lambda v1,v2: tuple(map(lambda a,b: a-b,v1,v2))

    antiNodePositions = set()
    for v1,v2 in combinations(antennas,2):
        dir = subVec(v2,v1)

        V1 = subVec(v1,dir)
        while inBounds(V1,gridSize):
            antiNodePositions.add( V1 )
            V1 = subVec(V1,dir)
        
        V2 = addVec(v2,dir)
        while inBounds(V2,gridSize):
            antiNodePositions.add( V2 )
            V2 = addVec(V2,dir)
    
    return antiNodePositions | antennas

def Solution(data):
    antennas = defaultdict(lambda: set())

    for y in range(len(data)):
        for x in range(len(data[y])):
            point = data[y][x]
            if point != '.':
                antennas[point].add((y,x))

    antiNodePositions = set()
    for freq in antennas.keys():
        antiNodePositions |= antiNodesP1( antennas[freq], (len(data),len(data[0])) )
    yield len(antiNodePositions)
    
    antiNodePositions = set()
    for freq in antennas.keys():
        antiNodePositions |= antiNodesP2( antennas[freq], (len(data),len(data[0])) )
    yield len(antiNodePositions)