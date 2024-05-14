# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from itertools import permutations
from bisect import bisect_right
    
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

def isPrime(n, maxN, primes):
    if n < 2:
        return False
    if n < maxN:
        counter=0
        while n > primes[counter] ** 2:
            if n % primes[counter] == 0:
                return False
            counter+=1
    else:
        counter=0
        while len(primes) > counter:
            if n % primes[counter] == 0:
                return False
            counter+=1
        curprime=primes[counter-1] + 2
        while curprime ** 2 < n:
            if n % curprime == 0:
                return False
            curprime +=2
    return True
    
def isPrime2(n):
    if n == 2 or n == 3:
        return True
    if n% 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):  # Only odd numbers
        if n% i == 0:
            return False
    return True

if __name__ == "__main__":
    t=int(input())
    nlist=[]
    for x in range(t):
        nlist.append(int(input()))
    
    maxN = max(nlist)
    
    logmaxN = int(math.log(maxN, 10))
    #print(logmaxN)
    maxPrime=10**5
    
    primes = generate_primes(maxPrime)
    
    pandigitals=[]
    for x in range(2, logmaxN+2):
        pandigitals+= list(permutations(range(1, x+1)))
    
    for x in range(len(pandigitals)):
        pandigitals[x]=int(''.join([str(y) for y in pandigitals[x]]))
    
    primePans=[]
    for x in pandigitals:
        if isPrime(x, maxPrime, primes):
            primePans.append(x)
    
    #print(primePans)
    
    for x in nlist:
        index = bisect_right(primePans, x)
        if index == 0:
            print(-1)
        else:
            print(primePans[index-1])