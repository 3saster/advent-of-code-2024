import re

def Part1(data):
    data = "".join(data)
    pairs = re.findall("mul\((\d+),(\d+)\)",data)
    return sum( int(n[0])*int(n[1]) for n in pairs )

def Part2(data):
    data = "".join(data)
    data = data.split("do()")
    relevantData = [d.split("don't()")[0] for d in data]
    return Part1(relevantData)

def Solution(lines):
    yield Part1(lines)
    yield Part2(lines)