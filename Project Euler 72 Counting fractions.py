#len(F_n) = len(F_n-1) + tot(n))
#len(F_0) = 1

def generateTotients(n):  # generate totient values for numbers under n
    A = list(range(0, n))
    
    for x in range(2, n):
        if A[x] == x:
            for y in range(x, n, x):
                A[y] = A[y]//x * (x-1)
    return A

if __name__ == "__main__":
    length=10**6
    
    arr=generateTotients(length)
    arr[0]-=1
    
    for x in range(1, length):
        arr[x]+=arr[x-1]
    
    for x in range(int(input())):
        print(arr[int(input())])
