# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

if __name__ == "__main__":
    
    n=int(input())
    
    myinputs = [True] * (n + 1)
    
    answer = 0
    
    for x in range(2, n+1):
        if myinputs[x]:
            exp = 2
            results=[]
            while x ** exp <= n:
                myinputs[x ** exp] = False
                results+=[y for y in range(2*exp, n*exp + 1, exp) if y > n]
                exp+=1
            answer+=len(set(results)) + n - 1
    
    print(answer)
