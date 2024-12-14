import operator
    
def isPossible(nums,goal,operatorSet):
    if len(nums) == 1:
        return nums[0] == goal
    else:
        for operator in operatorSet:
            if isPossible( [operator(nums[0],nums[1])]+nums[2:], goal, operatorSet ):
                return True
        return False


def Solution(data):
    nums = [[int(d) for d in row.split(': ')[1].split(' ')] for row in data]
    goal = [int(d) for row in data for d in row.split(': ')[0].split(' ')]

    yield sum([g for numberList,g in zip(nums,goal) if isPossible(numberList,g,{operator.__add__,operator.__mul__})])
    yield sum([g for numberList,g in zip(nums,goal) if isPossible(numberList,g,{operator.__add__,operator.__mul__,lambda a,b:int(f"{a}{b}")})])