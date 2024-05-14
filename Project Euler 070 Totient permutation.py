def generateTotients(n):  # generate totient values for numbers under n
    A = list(range(0, n))
    
    for x in range(2, n):
        if A[x] == x:
            for y in range(x, n, x):
                A[y] = A[y]//x * (x-1)
    return A

def isPermutation(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

if __name__ == "__main__":
    n = int(input())
    totients=generateTotients(n)
    
    minRatio=0
    for x in range(2, n):
        ratio=totients[x]/x  # min(n/phi(n)) --> max(phi(n)/n), slightly faster
        if ratio>minRatio:
            if isPermutation(x, totients[x]):
                minRatio=ratio
                sol=x
    print(sol)
