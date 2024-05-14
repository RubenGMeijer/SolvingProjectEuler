# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def generatePythTriplets(n):
    solutions=[0]*n
    for x in range(1, 2001):
        for y in range(1, x):
            if (x + y) % 2 == 1 and math.gcd(x, y) == 1:
                peri = 2*x**2 + 2*x*y
                if peri > n:
                    continue
                for z in range(peri, n, peri):
                    solutions[z]+=1
    return solutions

if __name__ == "__main__":
    t=int(input())
    nlist=[]
    for x in range(t):
        nlist.append(int(input()))
    
    maxN=max(nlist)
    
    solutions=generatePythTriplets(maxN+1)
    maxSols=[]
    current=0
    currentIdx=0
    
    for x in range(maxN+1):
        if solutions[x]>current:
            current=solutions[x]
            currentIdx=x
        maxSols.append(currentIdx)
    
    for x in nlist:
        print(maxSols[x])
