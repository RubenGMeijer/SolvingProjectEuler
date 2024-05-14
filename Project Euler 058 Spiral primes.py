import math
from bisect import bisect_left
import random

def solve(n):
    old = [1, 1, 1, 1]
    new = [3, 5, 7, 9]
    cprimes = 3
    ctotal = 5
    iterations=1
    
    while True:
        mid=new.copy()
        for y in range(4):
            new[y]=2*mid[y]-old[y]+8
            old[y]=mid[y]
            if isPrimeMR(new[y]):
                cprimes+=1
            ctotal+=1
        iterations+=1
        if cprimes/ctotal*100 < n:
            break
    return iterations*2+1
    
def isPrimeMR(n, k=4):
    if n == 2 or n == 3:
        return True
    if n% 2 == 0 or n < 2:
        return False
    
    r, d = 0, n-1
    while d % 2 == 0:
        r+=1
        d//=2
    
    for x in range(k):
        a = random.randint(2, n-2)
        b = pow(a, d, n)
        for y in range(r):
            c= pow(b, 2, n)
            if c == 1 and b != 1 and b != n-1:
                return False
            b=c
        if c != 1:
            return False
    return True
    
if __name__ == "__main__":
    print(solve(int(input())))
