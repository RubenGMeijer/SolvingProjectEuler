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

primes = generatePrimes(10000)

nlist=[]

t=int(input())
for x in range(t):
    nlist.append([int(input()), x])

s_nlist=sorted(nlist)

n=max(nlist)
divisors=1

solutionlist=[]

# N = p_1^x_1 + p_2^x_2 + ... --> N_divisors = (x_1+1)(x_2+1)*...

triangleno=1
counter=1

for y in s_nlist:
    x=y[0]
    while divisors <= x:
        index=0
        currentprime=primes[index]
        primem=1
        counter+=1
        triangleno+=counter
        residual=triangleno
        divisors=1
        
        while residual>=currentprime:
            if residual % currentprime == 0:
                primem+=1
                residual//=currentprime
            else:
                divisors*=primem
                if divisors>x:
                    solutionlist.append(triangleno)
                    break
                primem=1
                index+=1
                if index>=len(primes):
                    break
                currentprime=primes[index]
        else:
            divisors*=primem
            if divisors>x:
                solutionlist.append(triangleno)
                break
    else:
        solutionlist.append(triangleno)

for x in range(len(s_nlist)):
    s_nlist[x].append(solutionlist[x])
s_nlist.sort(key=lambda x: x[1])

for x in s_nlist:
    print(x[2])