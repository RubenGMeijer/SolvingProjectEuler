import math

def isPrimeMR(n, k=3):  # Miller-Rabin probabilistic primality test for n<3,215,031,751
    if n == 2 or n == 3:
        return True
    if n% 2 == 0 or n < 2:
        return False
    
    r, d = 0, n-1
    while d % 2 == 0:
        r+=1
        d//=2
    
    arr=[2, 3, 5, 7]  # n<3,215,031,751
    for a in arr:
        b = pow(a, d, n)
        for y in range(r):
            c= pow(b, 2, n)
            if c == 1 and b != 1 and b != n-1:
                return False
            b=c
        if c != 1:
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
    
def concatenatePrimePairs(primes):
    # check if 'p1'+'p2' and 'p2'+'p1' are prime for every prime in primes
    # if so, dict[p1] set .add(p2)
    pairs={}
    length=len(primes)
    
    for x in range(length):
        pairs[x]=set()
        for y in range(x+1, length):
            if isPrimeMR(int(str(primes[x]) + str(primes[y]))) and isPrimeMR(int(str(primes[y]) + str(primes[x]))):
                pairs[x].add(y)
    return pairs

def pairingPlus(multiples, pairs):
    # multiples: dict with keys: tuples of nth primes, values nth primes
    # pairs: dict with key, values nth primes
    # nth primes of which any combination concatenates to form prime
    #
    # yields plus: dict same as multiples except one more prime per set
    plus={}
    for x in multiples.keys():
        for y in multiples[x]:
            temp=multiples[x].intersection(pairs[y])
            if temp:
                plus[x + tuple([y])]=temp
    return plus

if __name__ == "__main__":
    n, k = map(int, input().split())
    primes= generate_primes(n)
    pairs= concatenatePrimePairs(primes)
    
    multiples=dict(zip([tuple([x]) for x in pairs.keys()], pairs.values()))  # turn keys into tuples
        
    for x in range(k-2):
        multiples=pairingPlus(multiples, pairs)
    
    solArr=[]
    for x in multiples.keys():
        keySum=0
        for y in x:
            keySum+=primes[y]
        for y in multiples[x]:
            solArr.append(keySum+primes[y])
    
    solArr.sort()
    
    for x in solArr:
        print(x)
    
    # print(primePairsIdx[1].intersection(primePairsIdx[3]))
