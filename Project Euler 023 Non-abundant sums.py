# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def prepareAbundant(n):
    sol=[False, 0] + [1]*(n-1)
    for x in range(2, n//2):
        for y in range(2*x, n, x):
            sol[y] += x
    for x in range(1, n+1):
        if sol[x] > x:
            sol[x] = True
        else:
            sol[x] = False
    return sol
    
if __name__ == "__main__":
    t = int(input())
    nlist=[]
    for x in range(t):
        nlist.append(int(input()))
    
    solbool = prepareAbundant(max(nlist))
    # print(solbool)
    
    for x in nlist:
        if x > 28123:
            print('YES')
        else:
            for y in range(-((x+1)//-2)):
                if (solbool[y] and solbool[x-y]) is True:
                    print('YES')
                    break
            else:
                print('NO')