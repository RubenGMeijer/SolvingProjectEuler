import math

def numberDigits(n):
    return math.ceil(math.log10(n))

def sqrt2Exp(iters):
    num=1
    den=1
    for x in range(1, iters+1):
        den_old=den
        den+=num
        num=den+den_old
        if numberDigits(num) > numberDigits(den):
            print(x)
    return num, den

if __name__ == "__main__":
    n=int(input())
    sqrt2Exp(n)
