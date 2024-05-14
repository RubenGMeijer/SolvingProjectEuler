
def generateCubes(n):
    cubeList=[]
    for x in range(n):
        cubeList.append(str(x**3))
    return cubeList
    
def categorizeCubes(cubeList):
    cubeDict={}
    for x in cubeList:
        tempKey=''.join(sorted(x))
        try:
            cubeDict[tempKey].append(x)
        except KeyError:
            cubeDict[tempKey]=[]
            cubeDict[tempKey].append(x)
    return cubeDict

if __name__ == "__main__":
    n, k = map(int, input().split())
    
    cubeDict=categorizeCubes(generateCubes(n))

    for x in cubeDict.values():
        if len(x) == k:
            print(x[0])
