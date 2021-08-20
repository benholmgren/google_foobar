def solution(l):
    # need to make a dynamic program to fulfill runtime reqs
    triples = 0
    # store the number of divisors found for each entry
    divs = [0]*len(l)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                divs[j] += 1
                triples += divs[i]
    return triples