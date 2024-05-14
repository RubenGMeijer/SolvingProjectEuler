# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

#  copy binarysearch later
def binarySearch(arr, x):  # returns index of x if it is in sorted array, else -1 
    low = 0
    high = len(arr)-1
    
    while high <= low:
        mid = (high+low) // 2
        if arr[mid] < x:  # element at right half of array
            low=mid+1
        elif arr[mid] > x:  # element at left half of array
            high=mid-1
        else:
            return mid
    else:
        return -1

def generateFactors(maxN):  # generate list with amount of distinct factors
    A = [0] * maxN
    for x in range(2, maxN):
        if not A[x]:
            for y in range(x, maxN, x):
                A[y] += 1
    return A
    
if __name__ == "__main__":
    n, k = map(int, input().split())

    factors=generateFactors(n+k)
    counter=0
    
    for x in range(n+k):
        if factors[x]==k:
            counter+=1
            if counter >=k:
                print(x-k+1)
        else:
            counter=0
