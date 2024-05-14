
def getways(n):
    a=[0]*(n+1)
    a[0]=1
    for x in range(1, n+1):
        for y in range(x, n+1):
            a[y]+=a[y-x]% (10**9+7)
    for x in range(n+1):
        a[x] = (a[x]-1) % (10**9+7)
    return a

def main():
    t=int(input())
    nlist=[]
    for x in range(t):
        nlist.append(int(input()))
    nmax=max(nlist)
    a = getways(nmax)
    for x in nlist:
        print(a[x])
    return

if __name__ == "__main__":
    main()
