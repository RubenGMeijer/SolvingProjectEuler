
def sternBrocotLeft(a=0, b=1, c=1, d=1, e=1, f=0):
    return [a, b, a+c, b+d, c, d]

def sternBrocotRight(a=0, b=1, c=1, d=1, e=1, f=0):
    return [c, d, c+e, d+f, e, f]

def sternBrocotCenter(a=0, b=1, c=1, d=1, e=1, f=0):
    return [a+c, b+d, c, d, c+e, d+f]

def solve(cref, dref, n):
    # solution is given by the stern-brocot tree
    # one entry to the left of input, given that den(result) <= n
    # returns result: [num, den]
    fracs=[0, 1, 1, 1, 1, 0]
    while True:
        # cref/dref < c/d & dref >= d --> cref*d < c*dref
        if cref*fracs[3] < fracs[2]*dref:
            fracs=sternBrocotLeft(*fracs)
        elif cref*fracs[3] > fracs[2]*dref:
            fracs=sternBrocotRight(*fracs)
        else:
            while fracs[1] <= n:
                abold = fracs[0:2].copy()
                fracs=sternBrocotCenter(*fracs)
            else:
                return abold

def eediv(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = eediv(b % a, a)
    return g, x - (b//a)*y, y

def modinv(a, b):
    g, x, y = eediv(a, b)
    if g != 1:
        raise Exception('gcd(a,b) != 1, no inverse')
    return x % b

if __name__ == "__main__":
    
    for x in range(int(input())):
        a, b, n = map(int, input().split())
        d = (n % b) - modinv(a, b)
        if d<0:
            d+=b
        den = n - d
        num = (den * a - 1) // b
        print(num, den)
        
