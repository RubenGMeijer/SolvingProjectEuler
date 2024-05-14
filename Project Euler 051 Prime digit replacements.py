from bisect import bisect_left
from itertools import combinations
import math
from collections import defaultdict


def generatePrimes(maxN):  # generate primes smaller than maxn
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

def countDigits(n):  # input int, returns count of each digit (0-9) in n as array
    arr=[0]*10
    while n:
        arr[n % 10] +=1
        n//=10
    return arr

if __name__ == "__main__":
    n, k, m = map(int, input().split())
    
    primesRaw = generatePrimes(10**n)
    primesRaw = primesRaw[bisect_left(primesRaw, 10**(n-1)):]  # select only n-digit primes
    
    primes=[]
    for x in primesRaw:  # eliminate primes that don't have k equal digits
        if any([y >= k for y in countDigits(x)]):
            primes.append(x)

    solArr=[]
    for x in reversed(list(combinations(range(n), k))):
        #  create hashmap of primes that are ddd**, dd*d*, ...
        primeDict=defaultdict(list)
        for y in primes:
            broken=False
            dictKey = list(str(y))
            
            targetDigit=dictKey[x[0]]
            dictKey[x[0]]='*'
            for z in x[1:]:
                if dictKey[z] != targetDigit:  # ensure replaced digits are the same
                    broken=True
                    break
                dictKey[z]= '*'
            if broken:
                continue
            dictKey=''.join(dictKey)
            primeDict[dictKey].append(y)
        
        #  select the first (= lexicographically smallest) set of primes for current combination of digit replacements
        for y in primeDict.values():
            if len(y)>=m:
                # print(y)
                solArr.append(' '.join(str(z) for z in y[:m]))  # prepare for printing
                break
    print(sorted(solArr)[0])
