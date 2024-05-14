# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from bisect import bisect_left

def primeSieve(n):
    sieve=[False, False, True]+[True]*(n-3)
    
    length=len(sieve)
    
    for x in range(length):
        if sieve[x]:
            for y in range(x**2, length, x):
                sieve[y] = False
    answer = [x for x in range(n) if sieve[x]]
    return answer

if __name__ == "__main__":
    n=int(input())
    
    myPow = int(math.log10(n))
    
    primes=primeSieve(10**myPow)
    countPrimes = len(primes)
    
    for x in reversed(range(len(primes))):
        if primes[x] < n:
            nIndex = x
            break
    
    answer=0
    
    for x in primes[:nIndex+1]:
        broken=False
        xStr = str(x)
        for y in range(1, len(xStr)):
            xStr = xStr[1:]+xStr[0]
            xRot = int(xStr)
            tempIdx = bisect_left(primes, xRot)  # cheeky janky binary search
            if tempIdx != countPrimes:
                if primes[tempIdx] != xRot:
                    broken=True
                    break
            else:
                broken=True
                break
                
        if not broken:
            answer+=x
    
    print(answer)
        

