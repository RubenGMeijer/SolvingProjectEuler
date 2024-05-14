def digitSum(n):
    s=0
    while n:
        s += n % 10
        n //= 10
    return s

def generateExpansionE(iters):
    if iters == 0:
        return []
    iterList=[1]
    if iters == 1:
        return iterList
    iters-=2
    for x in range(iters+1):
        if x % 3 == 0:
            iterList.append(x//3*2+2)
        else:
            iterList.append(1)
    return list(reversed(iterList))

def evalExpansion(init, arr):
    if arr == []:
        return init, 1
    num=1
    den=arr[0]
    for x in arr[1:]:
        num+=den*x
        num, den=den, num
    num+=init*den
    return num, den

if __name__ == "__main__":
    num, den = evalExpansion(2, generateExpansionE(int(input())-1))
    print(digitSum(num))
