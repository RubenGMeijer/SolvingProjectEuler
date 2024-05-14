# Enter your code here. Read input from STDIN. Print output to STDOUT

def generatePentagonals(n): # non-inclusive
    pentagonals=[]
    incr=1
    pent=0
    
    for x in range(n):
        pentagonals.append(pent)
        pent+=incr
        incr+=3
    return pentagonals
    
def isPentagonal(n):
    p = (1+(24*n +1) ** 0.5)/6
    if int(p) == p:
        return True
    return False

if __name__ == "__main__":
    n, k = map(int, input().split())
    
    ps=generatePentagonals(n)
    
    for x in range(k+1, n):
        if isPentagonal(ps[x]+ps[x-k]) or isPentagonal(ps[x]-ps[x-k]):
            print(ps[x])
        
        
