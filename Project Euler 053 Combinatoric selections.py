import math

if __name__ == "__main__":
    n, k = map(int, input().split())
    
    for x in range(n+1):
        if math.comb(x, x//2) > k:
            a, b = x, x//2
            break
    
    solutions=[]
    while a <= n:
        while math.comb(a, b) > k:
            b-=1
        else:
            b+=1
            solutions.append([a, b])
            a+=1
    
    counter=0
    for x in solutions:
        counter+=x[0]-(2*x[1])+1
    print(counter)
