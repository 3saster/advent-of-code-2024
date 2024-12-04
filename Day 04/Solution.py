from collections import Counter

def at(arr,y,x):
    if 0 <= y < len(arr):
        if 0 <= x < len(arr[y]):
            return arr[y][x]
    return None

def findWord(data,word):
    out = []

    for y in range(len(data)):
        for x in range(len(data)):
            if data[y][x] == word[0]:
                # Start looking for word
                for y_dir in [-1,0,1]:
                    for x_dir in [-1,0,1]:
                        if (y_dir,x_dir) == (0,0): continue
                        linePath = [(Y,X) for Y,X in zip([y+y_dir*i for i in range(len(word))],[x+x_dir*i for i in range(len(word))])]
                        line = [at(data,Y,X) for Y,X in linePath]
                        if None in line: continue
                        if "".join(line) == word:
                            out += [linePath]
    return out

def Part1(data):
    xmasWords = findWord(data,"XMAS")
    return len(xmasWords)

def Part2(data):
    crossCenters = []
    for y in range(len(data)):
        for x in range(len(data)):
            if data[y][x] == 'A':
                cross = Counter([at(data,y+1,x+1),at(data,y+1,x-1),at(data,y-1,x+1),at(data,y-1,x-1)])
                if {at(data,y+1,x+1),at(data,y-1,x-1)} == {'M','S'} and {at(data,y-1,x+1),at(data,y+1,x-1)} == {'M','S'}:
                    crossCenters.append((y,x))
    return len(crossCenters)