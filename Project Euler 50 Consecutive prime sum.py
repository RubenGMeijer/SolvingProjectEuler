# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from bisect import bisect_right
    
def isPrime2(n, primes):
    if n < 2:
        return False
    if n == 2:
        return True
    maxIdx=bisect_right(primes, int(n**0.5))+1
    for x in primes[:maxIdx]:
        if n % x == 0:
            return False
    return True
    
def generate_primes(maxN):  # generate primes smaller than maxn
    A = [True] * maxN
    A[0], A[1] = False, False
    maxPrime = math.floor(maxN ** 0.5)
    for x in range(2, maxPrime):
        if A[x]:
            for y in range(x**2, maxN, x):
                A[y] = False
    B = range(maxN)
    B = [x for x in range(maxN) if A[x]]
    return B

def solve(n, primes):
    counterR=-1
    primeSum=0
    while primeSum < n:
        counterR+=1
        primeSum+= primes[counterR]
    if primeSum > n:
        primeSum-= primes[counterR]
        counterR-=1
        
    while True:
        if isPrime2(primeSum, primes):
            break
        primeSum-=primes[counterR]
        counterR-=1
    
    counterL=0
    currentmax = [primeSum, counterL, counterR]
    counterL+=1
    counterR=1+currentmax[2] + counterL - currentmax[1]
    primeSum=sum(primes[counterL:counterR+1])

    while primeSum <= n:
        while primeSum <= n:
            if isPrime2(primeSum, primes):
                currentmax = [primeSum, counterL, counterR]
            counterR+=1
            primeSum+= primes[counterR]

        counterL+=1
        counterR=1+currentmax[2] + counterL - currentmax[1]
        primeSum=sum(primes[counterL:counterR+1])
    return [currentmax[0], currentmax[2]-currentmax[1]+1]
            

if __name__ == "__main__":
    primes = generate_primes(10**7)
    
    for _ in range(int(input())):
        arr = solve(int(input()), primes)
        print(' '.join(map(str, arr)))