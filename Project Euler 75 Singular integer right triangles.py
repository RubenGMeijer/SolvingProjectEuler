
from math import gcd, sqrt
from bisect import bisect_right

def generateTriplets(length):
    triplets=set()
    multiples=set()
    for x in range(2, int(sqrt(length/2))+1):
        for y in range(1+x %2, min(x, length//(2*x)-x+1), 2):
            if gcd(x, y) > 1:
                continue
            a = x**2 - y**2
            b = 2*x*y
            c = x**2 + y**2
            for k in range(1, length//(a+b+c)+1):
                triplet = k*a+k*b+k*c
                if triplet in triplets:
                    multiples.add(triplet)
                else:
                    triplets.add(triplet)
    triplets = triplets.difference(multiples)
    return sorted(list(triplets))
                
def main():
    t=int(input())
    nlist=[]
    for x in range(t):
        nlist.append(int(input()))
    nmax=max(nlist)
    triplets = generateTriplets(nmax)
    
    for x in nlist:
        print(bisect_right(triplets, x))
    return

if __name__ == "__main__":
    main()
