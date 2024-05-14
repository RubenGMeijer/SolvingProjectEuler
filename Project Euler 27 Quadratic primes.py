# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def generate_primes(maxN):  # generate primes smaller than maxn
    A = [True] * maxN
    A[0], A[1] = False, False
    maxPrime = math.floor(maxN ** 0.5)
    for x in range(2, maxPrime):
        if A[x] is True:
            for y in range(x **2, maxN, x):
                A[y] = False
    B = range(maxN)
    B = [z for z in list(map(lambda x, y: x*y, A, B)) if z != 0]
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
    return True

if __name__ == "__main__":
    maxN = 10**4
    primes = generate_primes(maxN)
    
    lim=int(input())
    
    if lim % 2 == 0:
        lowerlim=-lim+1
    else:
        lowerlim=-lim
    
    maxa=0
    maxb=0
    maxseq=0
    
    for a in range(lowerlim, lim, 2):
        for b in generate_primes(lim+1):
            counter=1
            while True:
                if isPrime((counter ** 2 + counter*a + b), maxN, primes):
                    counter+=1
                else:
                    if counter > maxseq:
                        maxseq = counter
                        maxa=a
                        maxb=b
                    break
    
    print(maxa, maxb)
                    
    
    
    
