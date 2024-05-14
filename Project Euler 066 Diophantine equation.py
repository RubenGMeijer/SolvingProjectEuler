import math

def seriesExpand1(a, b, c, d):
    # takes: a + (b / (sqrt(c) + d))
    # returns: e + (f / sqrt(c) + h) # one series expansion cycle
    e = int(b / (math.sqrt(c) + d))  # ensure remainder < 1
    f = (c - d ** 2)//b
    h = -d - e * f
    return e, f, c, h
    
def seriesExpand(c):
    # uses seriesExpand1 until b and d repeat, returns continued fraction expansion and period
    a= int(math.sqrt(c))
    if a ** 2 == c:
        return a, [], 0
    a0, b, d, d0 = a, 1, -a, -a
    
    series=[]
    period=0
    
    while True:
        a, b, c, d = seriesExpand1(a, b, c, d)
        series.append(a)
        period+=1
        if b == 1 and d == d0:
            return a0, series, period

def evalExpansion(init, arr):
    # evaluates finite continued fraction expansion and returns corresponding num/den
    # see: continued fraction wikipedia
    arr=list(reversed(arr))
    if arr == []:
        return init, 1
    num=1
    den=arr[0]
    for x in arr[1:]:
        num+=den*x
        num, den=den, num
    num+=init*den
    return num, den

def solve(d):
    # see wikipedia
    # https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions
    # returns the fundamental integer solution to Pell's equation x**2 - d y**2 = 1
    init, series, period = seriesExpand(d)
    if period % 2 == 1:
        series += series
    if not series:
        return -1
    series.pop(-1)
    
    num, den = evalExpansion(init, series)
    return num

if __name__ == "__main__":
    maxsol=0
    maxD=0
    for d in range(int(input())+1):
        sol=solve(d)
        if sol > maxsol:
            maxsol = sol
            maxD=d
    
    print(maxD)
