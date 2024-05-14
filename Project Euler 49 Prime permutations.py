# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from bisect import bisect_left
from collections import defaultdict

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n% 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):  # Only odd numbers
        if n% i == 0:
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

def binarySearch(arr, x):  # returns index of x if it is in sorted array, else -1 
    low = 0
    high = len(arr)-1
    
    while high <= low:
        mid = (high+low) // 2
        if arr[mid] < x:  # element at right half of array
            low=mid+1
        elif arr[mid] > x:  # element at left half of array
            high=mid-1
        else:
            return mid
    else:
        return -1

if __name__ == "__main__":
    n, k = map(int, input().split())
    primes = generate_primes(10**len(str(n-1)))
    
    # create dictionary/hashmap containing prime anagram sets
    leftindex = bisect_left(primes, 1400)
    primeDict=defaultdict(list)
    solArr=[]
    
    
    for x in primes[leftindex:]:
        primeDict[''.join(sorted(str(x)))].append(x)

    for x in primeDict.values():
        for y in range(len(x)-k+1):
            for z in range(y+1, len(x)-k+2):
                cArr=[]
                a = x[y]
                b = x[z]-a
                for z2 in range(k-2):
                    c=a+(2+z2)*b
                    if c in x[z:]:
                        cArr.append(c)
                    else:
                        break
                else:
                    if a > n:  # probably not optimized
                        break
                    solArr.append([x[y], x[z]]+ cArr)
    
    solArr.sort()
    
    for x in solArr:
        print(''.join(map(str, x)))