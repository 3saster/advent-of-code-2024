from collections import Counter

def Part1(data):
    data = [[int(n) for n in l.split()] for l in data]
    first  = sorted( [d[0] for d in data] )
    second = sorted( [d[1] for d in data] )

    return sum( abs(s-f) for f,s in zip(first,second) )

def Part2(data):
    data = [[int(n) for n in l.split()] for l in data]
    first  = [d[0] for d in data]
    second = Counter([d[1] for d in data])
    
    return sum( f*second[f] for f in first )

def Solution(lines):
    yield Part1(lines)
    yield Part2(lines)