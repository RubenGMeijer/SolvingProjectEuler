import math

def countDigits(n):
    return int(math.log10(n))+1
    
def countPowerDigits(n):
    counter=1
    while True:
        power = counter**n
        length = countDigits(power)
        if length > n:
            return
        if length == n:
            print(power)
        counter+=1

if __name__ == "__main__":
    countPowerDigits(int(input()))
