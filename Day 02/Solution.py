def isSafe(arr,tol=0):
    if tol == 0:
        sign = -1 if arr[0] - arr[-1] > 0 else 1

        for n in range(1,len(arr)):
            if not (1 <= sign*(arr[n] - arr[n-1]) <= 3):
                return False
        return True
    else:
        for n in range(len(arr)):
            newArr = arr[:n] + arr[n+1:]
            if isSafe(newArr,tol-1):
                return True
        return isSafe(arr,tol-1)

def Part1(data):
    data = [[int(n) for n in l.split()] for l in data]
    return sum(1 for report in data if isSafe(report))

def Part2(data):
    data = [[int(n) for n in l.split()] for l in data]
    return sum(1 for report in data if isSafe(report,1))