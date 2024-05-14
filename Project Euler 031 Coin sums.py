# Enter your code here. Read input from STDIN. Print output to STDOUT

def combinations(n, coins):
    arr = [1]+[0]*n
    myMod = 10**9 + 7
    
    for x in coins:
        for y in range(n-x +1):
            arr[y+x]+= arr[y]
    
    for x in range(len(arr)):
        arr[x] %= myMod
    return arr
    
if __name__ == "__main__":
    
    myCoins = [1, 2, 5, 10, 20, 50, 100, 200]
    
    t = int(input())
    nlist=[]
    for x in range(t):
        nlist.append(int(input()))
    
    myCombinations = combinations(max(nlist), myCoins)
    
    for x in nlist:
        print(myCombinations[x])
