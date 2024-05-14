# Enter your code here. Read input from STDIN. Print output to STDOUT

def intToBase(n, b):  # returns '' if zero
    myString = ''
    while n:
        myString += str(n % b)
        n //=b
    return myString
    
if __name__ == "__main__":
    
    n, b = map(int, input().split())
    
    palindromes = []
    
    for x in range(n):
        if str(x) == str(x)[::-1]:
            palindromes.append(x)
    
    answer=0
            
    for x in palindromes:
        y = intToBase(x, b)
        if str(y) == str(y)[::-1]:
            answer+=x
    
    print(answer)
