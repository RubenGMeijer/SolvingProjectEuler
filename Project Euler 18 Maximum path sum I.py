t=int(input())

def reduceTree(slice1, slice2): # reducing upwards
    for x in range(len(slice1)):
        slice1[x]+=max(slice2[x], slice2[x+1])
    return slice1

for x in range(t):
    n=int(input())
    tree = []
    for y in range(n):
        tree.append(list(map(int, input().split())))
    
    for y in reversed(range(n-1)):
        tree[y] = reduceTree(tree[y], tree[y+1])
    print(tree[0][0])
