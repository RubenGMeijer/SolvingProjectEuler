import math
from itertools import permutations

def countDigits(n):
    return int(math.log10(n))+1

def genPolyNo(s):
    # generate 4-digit polygonal numbers given sides of polygon s
    inc=s-2
    n=0
    c=0
    sol=[]
    while True:
        c+=1+n*inc
        n+=1
        if countDigits(c) > 4:
            return sol
        if countDigits(c) > 3:
            sol.append(c)

def isCyclic(n1, n2):
    if str(n1)[-2:] == str(n2)[0:2]:
        return True
    return False

def solve(arr):
    polygons={}
    # arr2=arr.copy()
    for x in arr:
        polygons[x]=genPolyNo(x)
    
    start=arr.pop()                          # as the series are cyclic,
    startArr=[[x] for x in polygons[start]]  # it doesn't matter which polygonal series starts
    newArr=[]
    solArr=[]
    
    # 1 choose a start collection of gonal numbers
    # 2 choose any series of gonal number collections to follow
    # 3 take all combinations of numbers in start and follow that are cyclic
    # 4 repeat until chains are formed
    # 5 check if the first link is cyclic to the last link
    # 6 repeat #2 until all possible permutations are exhausted
    for a in permutations(arr):
        oldArr=startArr.copy()
        for b in a:
            for c in oldArr:
                for d in polygons[b]:
                    if isCyclic(c[-1], d):
                        newArr.append(c.copy())
                        newArr[-1].append(d)
            oldArr=newArr.copy()
            newArr=[]
        for e in oldArr:
            if isCyclic(e[-1], e[0]):
                solArr.append(e)
    
    [x.sort for x in solArr]  # remove duplicate series
    solArr=set(tuple(x) for x in solArr)
    
    sumArr=[]
    for x in solArr:
        if len(set(x)) == len(x):  # remove series with duplicate elements
            sumArr.append(sum(x))
    sumArr.sort()
    return sumArr

if __name__ == "__main__":
    t=int(input())
    arr=list(map(int, input().split()))
    sumArr=solve(arr)

    for x in sumArr:
        print(x)
