# Enter your code here. Read input from STDIN. Print output to STDOUT

def powerDigit(n, power):
    nstr = str(n)
    result=0
    
    for x in nstr:
        result+=int(x) ** power
    
    if n == result:
        return True
    else:
        return False

if __name__ == "__main__":
    power = int(input())
    
    answer=0
    for x in range(2, 8*10 ** power):
        if powerDigit(x, power):
            answer+=x
    
    print(answer)
