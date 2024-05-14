# Enter your code here. Read input from STDIN. Print output to STDOUT

def multiplyPandigital(n, k):
    if n <2:
        raise Exception("n must be at least 2")
    
    digits=str(n)
    counter=2
    while len(digits) < k:
        digits += str(n*counter)
        counter+=1
    return isPandigital(digits, k)

def isPandigital(digits, k):
    reference = [0]*10
    reference[1:k+1] = [1 for _ in range(k)]
    current = [0]*10
    
    for x in list(digits):
        current[int(x)]+=1
    if reference == current:
        return True
    return False
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    
    #print(multiplyPandigital(18, 8))
    
    for x in range(2, n):
        if multiplyPandigital(x, k):
            print(x)
