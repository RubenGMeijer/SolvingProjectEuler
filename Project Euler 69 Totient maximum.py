import math

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

def solve(n, primes):
    counter=1
    for x in primes:
        if counter*x >= n:
            return counter
        counter*=x
    else:
        return "Prime library too small"
    
if __name__ == "__main__":
    primes=generatePrimes(1000)
    for x in range(int(input())):
        print(solve(int(input()), primes))
