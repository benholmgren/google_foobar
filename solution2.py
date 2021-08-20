def solution(l, t):
    # Make a window into the list that moves left to right as sums get too large
    windowSum = l[0]
    left = 0
    right = 1

    # list of candidate indices to find smallest lex subarray
    candIdx = []

    while right <= len(l):
        # if our window still makes sense, and sums to something too large
        while left < right - 1 and windowSum > t:
            windowSum = windowSum - l[left]
            left += 1

        # if we're on the money
        if windowSum == t:
            candIdx.append([left, right - 1])
        # if we haven't checked the whole list yet
        if right < len(l):
            windowSum += l[right]

        right += 1

    minCand = [1000000]
    minIdx = [1000000, 1000000]
    for window in candIdx:
        # For the simple solution, I'll just use built in sorting methods
        # Normally, one might implement this themselves to save a logarithmic term in runtime if it was of concern
        windowContents = l[window[0]:window[1] + 1]
        windowContents.sort(reverse=True)
        if minCand > windowContents:
            minIdx = window
            minCand = windowContents

    # if we never found a sum
    if len(candIdx) == 0:
        minIdx = [-1, -1]

    return minIdx
