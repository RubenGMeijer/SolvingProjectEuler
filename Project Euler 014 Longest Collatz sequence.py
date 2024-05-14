t = int(input())
n=[int(input()) for x in range(t)]
maxn=max(n)

results=[None]*(maxn+1)
results[0], results[1] = 0, 1
maxnumbers=results.copy()

for x in range(2, maxn+1):
    i = x
    count=0
    while i >= x:
        if i % 2 == 0:
            i //= 2
            count+=1
        else:
            i = (3*i+1)//2
            count+=2
    else:
        results[x]=results[i] + count

cmax=1
cindex=1
for x in range(2, maxn+1):
    if results[x] >= cmax:
        cindex=x
        cmax = results[x]
    maxnumbers[x]=cindex

for x in n:
    print(maxnumbers[x])
