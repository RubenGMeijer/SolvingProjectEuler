from math import factorial

chainDict ={
    1: 1,
    2: 1,
    145: 1,
    169: 3,
    363601: 3,
    1454: 3,
    871: 2,
    45361: 2,
    872: 2,
    45362: 2,
    40585: 1
}

factorials = [factorial(x) for x in range(10)]  # precalculate values

def factorialDigits(n):
    sum=0
    for x in str(n):
        sum+=factorials[int(x)]
    return sum

def getChain(n):
    chain=[]
    while True:
        if n in chainDict:
            counter=chainDict[n]+1
            break
        else:
            chain.append(n)
            n=factorialDigits(n)
    # update dictionary
    for x in reversed(chain):
        chainDict[x] = counter
        counter+=1
    return

def solve(n, le):
    solArr=[]
    for x in range(n+1):
        if x not in chainDict:
            getChain(x)
        if chainDict[x] == le:
            solArr.append(x)
    return solArr

def main():
    t = int(input())
    for x in range(t):
        n, le = map(int, input().split())
        sol=solve(n, le)
        if sol == []:
            sol = [-1]
        sol=list(map(str, sol))
        print(' '.join(sol))

if __name__ == "__main__":
    main()
