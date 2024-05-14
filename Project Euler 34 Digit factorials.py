# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def digitFactorials():
    answer=[]
    for x in range(0, 10):
        answer.append(math.factorial(x))
    return answer

if __name__ == "__main__":
    n = int(input())
    factorials = digitFactorials()
    
    answerSum=0
    
    for x in range(10, n):
        facSum=0
        for y in map(int, str(x)):
            facSum+= factorials[y]
        if facSum % x == 0:
            answerSum+= x
    
    print(answerSum)
