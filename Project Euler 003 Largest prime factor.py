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

if __name__ == "__main__":
    primes = generatePrimes(10000)
    
    t = int(input().strip())
    for x in range(t):
        n = int(input().strip())
        nsqr=int(n**0.5)+1
        counter=0
        length=len(primes)
        broken=False
        foundfactor=False
        
        while n >= primes[counter]:
            if n % primes[counter] == 0:
                n=n//primes[counter]
                largestprime=primes[counter]
            else:
                counter+=1
            if counter >= length:
                broken = True
                break
        
        if broken:
            x=primes[length-1]
            while nsqr >= x:
                if n % x == 0:
                    n=n//x
                    largestprime=x
                    foundfactor=True
                else:
                    x+=2
        if not broken:
            print(largestprime)
        elif foundfactor:
            print(largestprime)
        else:
            print(n)
