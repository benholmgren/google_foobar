def solution(x, y):
    distToEnd = y - 1
    # compute out the base
    id = 0
    i = 1
    prev = 0
    while i <= x + distToEnd:
        id = i + prev
        i += 1
        prev = id
    return id - distToEnd