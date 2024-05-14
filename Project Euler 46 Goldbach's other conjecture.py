# Enter your code here. Read input from STDIN. Print output to STDOUT

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):  # Only odd numbers
        if n% i == 0:
            return False
    return True

def goldbachCounter(n):
    counter=0
    square=1
    potentialPrime = n - 2 * square ** 2
    
    while potentialPrime > 1:
        if isPrime(potentialPrime):
            counter+=1
        square+=1
        potentialPrime = n - 2 * square ** 2
    return counter

if __name__ == "__main__":
    for _ in range(int(input())):
        print(goldbachCounter(int(input())))
