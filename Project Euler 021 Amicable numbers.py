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

def primeFactorization(n, primes):
    idx = 0
    resultslist=[]
    while n > primes[idx] ** 2:
        counter=0
        while n % primes[idx] == 0:
            counter+=1
            n //= primes[idx]
        else:
            if counter != 0:
                resultslist.append([counter, primes[idx]])
            idx +=1
    return resultslist

if __name__ == "__main__":
    t=int(input())
    nlist=[]
    for x in range(t):
        nlist.append(int(input()))
    
    nmax=max(nlist)
    
    divs = [0, 0] + [1]*(nmax)
    sol = [0]*(nmax+1)
    
    for x in range(2, nmax//2):
        for y in range(2*x, nmax+1, x):
            divs[y]+=x
    
    for x in range(1, nmax+1):
        sol[x]=sol[x-1]
        if divs[x] < nmax:
            if divs[x] != x:
                if x == divs[divs[x]]:
                    sol[x]+=x
    
    for x in nlist:
        print(sol[x])