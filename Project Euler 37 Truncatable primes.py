# Enter your code here. Read input from STDIN. Print output to STDOUT

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
    
if __name__ == "__main__": # maybe not the best to use primeStr
    
    n = int(input())
    primes = primeSieve(n)
    answer=0
    
    for x in range(4, len(primes)):  # starts at 4 to omit single digit primes
        primeStr=str(primes[x])
        broken = False
        while len(primeStr) > 1:
            primeStr = primeStr[1:]
            truncPrime = int(primeStr)
            tempIdx = bisect_left(primes[:x], truncPrime)  # cheeky janky binary search
            if primes[tempIdx] != truncPrime:
                broken = True
                break
        if broken:
            continue
        
        primeStr = str(primes[x])
        while len(primeStr) > 1:
            primeStr = primeStr[:-1]
            truncPrime = int(primeStr)
            tempIdx = bisect_left(primes[:x], truncPrime)  # cheeky janky binary search
            if primes[tempIdx] != truncPrime:
                broken = True
                break
                
        if not broken:
            answer+=primes[x]
    
    print(answer)
    
