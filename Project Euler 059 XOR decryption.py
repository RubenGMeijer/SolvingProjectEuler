
def solve(codes):
    
    solution=''
    misc=[32, 33, 39, 40, 41, 44, 45, 46, 63]
    
    for x in range(3):
        for y in range(97, 123):
            for z in codes[x::3]:
                d = y ^ z
                if not (122 >= d >= 97 or 90 >= d >= 65 or 59 >= d >= 48 or d in misc):
                    break
            else:
                solution+=chr(y)
                break
    return solution
    
if __name__ == "__main__":
    n=int(input())
    codes=list(map(int, input().split()))
    print(solve(codes))
