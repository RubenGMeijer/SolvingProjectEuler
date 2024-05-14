import math

def seriesExpand1(a, b, c, d):
    # takes: a + (b / (sqrt(c) + d))
    # returns: e + (f / sqrt(c) + h) # one series expansion cycle
    e = int(b / (math.sqrt(c) + d))  # ensure remainder < 1
    f = (c - d ** 2)//b
    h = -d - e * f
    return e, f, c, h
    
def seriesExpand(c):
    a= int(math.sqrt(c))
    if a ** 2 == c:
        return 0
    b, d, d0 = 1, -a, -a
    period=0
    
    while True:
        a, b, c, d = seriesExpand1(a, b, c, d)
        period+=1
        if b == 1 and d == d0:
            return period

def main(n):
    counter=0
    for x in range(2, n+1):
        if seriesExpand(x) % 2 != 0:
            counter+=1
    return counter

if __name__ == "__main__":
    print(main(int(input())))
        
