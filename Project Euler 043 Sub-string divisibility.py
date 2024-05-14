# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

def generatePandigitalTuples(n): # generates pandigitals of n length including 0
    return list(permutations(range(0, n)))

def divisiblePandigital(ptuple, length):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for x in range(1, length-2):
        if int(''.join([str(y) for y in ptuple[x:x+3]])) % primes[x-1] != 0:
            return False
    return True

if __name__ == "__main__":
    n=int(input())
    
    pandigitals = generatePandigitalTuples(n+1)
    
    counter=0
    
    for x in pandigitals:
        if divisiblePandigital(x, n+1):
            counter+=int(''.join([str(y) for y in x]))
    
    print(counter)
    
