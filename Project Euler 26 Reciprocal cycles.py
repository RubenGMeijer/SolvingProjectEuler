# Enter your code here. Read input from STDIN. Print output to STDOUT

def findRecurring(n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    if n == 1:
        return 0
    digits=1
    remainder=1
    while True:
        remainder*=10
        remainder = remainder % n
        if remainder == 1:
            break
        digits+=1
    return digits
        
if __name__ == "__main__":
    
    t = int(input())
    nlist=[]
    for x in range(t):
        nlist.append(int(input()))
    nmax=max(nlist)
    
    sollist=[0, 0, 0, 0]
    maxdigits=0
    answer=0
    for x in range(3, nmax):
        digits = findRecurring(x)
        if digits > maxdigits:
            answer=x
            maxdigits=digits
        sollist.append(answer)
        
    for x in nlist:
        print(sollist[x])
