
def countDigits(n):  # input int, returns count of each digit (0-9) in n as array
    arr=[0]*10
    while n:
        arr[n % 10] +=1
        n//=10
    return arr

def solve(n, k):
    solutions=[]
    
    for x in range(1, n+1):
        digitsArr = countDigits(x)
        for y in range(2, k+1):
            if countDigits(x*y) != digitsArr:
                break
        else:
            tempSol=[]
            for y in range(1, k+1):
                tempSol.append(str(x*y))
            solutions.append(tempSol)
    return solutions
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    solutions = solve(n, k)
    for x in solutions:
        print(' '.join(x))
