# Enter your code here. Read input from STDIN. Print output to STDOUT

def isPandigital(numberStr, target):  # type numberStr :  String
    digits = '123456789'
    targetDigits = set(digits[:target])
    if len(numberStr) != target:
        return False
    if set(numberStr) == targetDigits:
        return True
    return False

def solution(n):
    cLen = n // 2
    digits = '123456789'
    cMin = int(digits[:cLen])
    cMax = 10**cLen  # non-inclusive limit
    
    # c = a * b
    # len(c) = len(a) + len(b) (if n even) | len(c) = len(a) + len(b) + 1 (if n odd)
    # it follows that if len(a) < len(b), len(a) = n // 4 for 9 > n > 4
    
    aMaxLen = n // 4
    aMax = 10 ** (aMaxLen)  # non-inclusive limit
    
    products=set()
    
    for a in range(1, aMax):
        aLen = len(str(a))
        bLen = n - aLen - cLen
        for b in range(10**(bLen-1), 10**bLen):
            c = a * b
            if cMax > c >= cMin:
                if isPandigital(str(c)+str(b)+str(a), n):
                    products.add(c)
    return sum(products)

if __name__ == "__main__":
    print(solution(int(input())))

