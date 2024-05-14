# Enter your code here. Read input from STDIN. Print output to STDOUT

def findIndex(n):
    x=0
    while n > 0:
        x+=1
        n-=9*x*10**(x-1)
    else:
        n+=9*x*10**(x-1)
    
    temp=(n-1)//x
    ans=str(10**(x-1)+temp)[n-temp*x-1]
    return int(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        answer=1
        for x in list(map(int, input().split())):
            answer*=findIndex(x)
        print(answer)
    
