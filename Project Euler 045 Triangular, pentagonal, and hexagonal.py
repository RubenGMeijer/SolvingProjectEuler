# Enter your code here. Read input from STDIN. Print output to STDOUT

def generateOrthogonals(k, incr=1, no=0):
    no+=incr
    incr+=k-2
    return incr, no

def isOrthogonal(t, k):
    if k == 3:
        n=((8 *t+1) ** 0.5 -1)/2
    elif k == 5:
        n=((24*t+1) ** 0.5 +1)/6
    else:
        raise Exception("k must be 3 or 5")
    if int(n) == n:
        return True
    return False

if __name__ == "__main__":
    n, a, b = map(int, input().split())
    
    incr, no = generateOrthogonals(b)
    
    while no < n:
        if isOrthogonal(no, a):
            print(no)
        incr, no = generateOrthogonals(b, incr, no)