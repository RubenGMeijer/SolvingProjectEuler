import sys
import bisect

t = int(input().strip())

nlist=[]
for a0 in range(t):
    nlist.append(int(input().strip()))

pfound=1
primes=[2]
counter=3
primesneeded=max(nlist)

while pfound < primesneeded:
    if all(counter % x != 0 for x in primes[:bisect.bisect_left(primes, counter**0.5+1)]):
        primes.append(counter)
        pfound+=1
    counter+=1

#print(primes)
        
for x in nlist:
    print(primes[x-1])
