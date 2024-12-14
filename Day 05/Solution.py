from collections import defaultdict

def parseData(data):
    rules = defaultdict(lambda: [])
    pageLists = []

    i = 0
    while data[i] != "":
        rule = [int(n) for n in data[i].split('|')]
        rules[rule[0]] += [rule[1]]

        i += 1

    i += 1
    while i < len(data):
        pageLists.append( [int(n) for n in data[i].split(',')] )
        i += 1
    return rules,pageLists

def isSorted(pageList,rules):
    index = {n:i for i,n in enumerate(pageList)}
    for i,n in enumerate(pageList):
        if n in rules.keys():
            successors = [index[after] for after in rules[n] if after in index.keys()]
            if successors and min(successors) < i:
                return False
    return True

def sortTop(pageList,rules):
    outList = list(pageList)

    index = {n:i for i,n in enumerate(outList)}

    i = 0
    while i < len(outList):
        n = outList[i]
        if n in rules.keys():
            successors = [index[after] for after in rules[n] if after in index.keys()]
            if successors and (i2:=min(successors)) < i:
                n1,n2                  = outList[i],outList[i2]
                index[n1],index[n2]    = i2,i
                outList[i],outList[i2] = outList[i2],outList[i]
                i = 0
                continue
        i += 1
    return outList
            
def Part1(data):
    rules,pageLists = parseData(data)
    mid = [pageList[len(pageList)//2] for pageList in pageLists if isSorted(pageList,rules)]
    return sum(mid)

def Part2(data):
    rules,pageLists = parseData(data)
    mid = [sortTop(pageList,rules)[len(pageList)//2] for pageList in pageLists if not isSorted(pageList,rules)]
    return sum(mid)

def Solution(lines):
    yield Part1(lines)
    yield Part2(lines)
