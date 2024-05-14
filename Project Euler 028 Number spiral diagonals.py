# Enter your code here. Read input from STDIN. Print output to STDOUT

def myfunc(n):
    return ((4*n*(n+1)*(2*n+1)//6+n*(n+1)//2+n+1)*4-3) % (10**9+7)
    
    
if __name__ == "__main__":
    
    t=int(input())
    for x in range(t):
        print(myfunc(int(input())//2))