import math

def solution(n):
    n = int(n)
    exp = math.log(n, 2)
    moves = 0
    if not exp.is_integer():
        upper = math.ceil(exp)
        lower = math.floor(exp)
        distToUpper = math.pow(2, upper) - n
        distToLower = n - math.pow(2, lower)
        if distToUpper < distToLower:
            moves += distToUpper
            moves += upper
        else:
            moves += n - math.pow(2, lower)
            moves += lower
    else:
        moves += exp

    return int(moves)