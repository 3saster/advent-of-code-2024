from dataclasses import dataclass
from copy import deepcopy
from itertools import accumulate

@dataclass
class File:
    ID:     int
    length: int
    empty:  int

def compactDiskMapP1(diskMap: File):
    compactedDiskMap = deepcopy(diskMap)

    firstEmpty = lambda dMap: next((i for i,f in enumerate(dMap) if f.empty > 0), None)
    
    while (ind:=firstEmpty(compactedDiskMap)) != None:
        back = compactedDiskMap[-1]

        if back.length == 0:
            compactedDiskMap.pop(-1)
            continue
        
        if back.length <= compactedDiskMap[ind].empty:
            compactedDiskMap.insert(ind+1, File(back.ID,back.length,compactedDiskMap[ind].empty-back.length) )
            compactedDiskMap.pop(-1)
            compactedDiskMap[ind].empty = 0
        else:
            compactedDiskMap.insert(ind+1, File(back.ID,compactedDiskMap[ind].empty,0) )
            compactedDiskMap[-1].length = back.length - compactedDiskMap[ind].empty
            compactedDiskMap[ind].empty = 0
    return compactedDiskMap

def compactDiskMapP2(diskMap: File):
    compactedDiskMap = deepcopy(diskMap)

    firstEmpty = lambda dMap,size: next((i+1 for i,f in enumerate(dMap) if f.empty >= size), None)

    for ID in range(max(f.ID for f in compactedDiskMap),-1,-1):
        ind = next((i for i,f in enumerate(compactedDiskMap) if f.ID == ID), None)
        if ind != None and (front:=firstEmpty(compactedDiskMap,compactedDiskMap[ind].length)) != None and front <= ind:
            back = compactedDiskMap[ind]

            compactedDiskMap[ind-1].empty += back.length+back.empty
            compactedDiskMap.insert(front,File(back.ID,back.length,compactedDiskMap[front-1].empty-back.length))
            compactedDiskMap[front-1].empty = 0
            compactedDiskMap.pop(ind+1)
    return compactedDiskMap

def checksum(diskMap):
    indexes = [0] + list(accumulate([f.length+f.empty for f in diskMap]))
    return sum([sum(i for i in range(indexes[i],indexes[i]+f.length))*f.ID for i,f in enumerate(diskMap)])

def parseData(diskMap):
    newDiskMap = []
    for i in range(0,len(diskMap),2):
        try:
            newDiskMap += [File(i//2,int(diskMap[i]),int(diskMap[i+1]))]
        except IndexError:
            newDiskMap += [File(i//2,int(diskMap[i]),0)]
    return newDiskMap


def Solution(data):
    diskMap = parseData(data[0])

    yield checksum( compactDiskMapP1(diskMap) )
    yield checksum( compactDiskMapP2(diskMap) )