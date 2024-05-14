import sys

t = int(input().strip())
nlist=[]

for a0 in range(t):
    nlist.append(int(input().strip()))
    largestn=max(nlist)+1

primes=[0, 0]
primes.extend(list(range(2, largestn)))

index=-1
for x in primes:
    index+=1
    if x !=0:
        for y in range(2*index, largestn, index):
            primes[y]=0

for x in range(1, len(primes)):
    primes[x]+=primes[x-1]

#print(primes)
for x in nlist:
    print(primes[x])
