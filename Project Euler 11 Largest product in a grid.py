import sys
import math

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
   
hno=0
for x in range(20):
    for y in range(20):
        u, le, dl, dr = 0, 0, 0, 0
        if y < 17:
            le=math.prod(grid[x][y:y+4])
        if x < 17:
            u=grid[x][y]*grid[x+1][y]*grid[x+2][y]*grid[x+3][y]
        if x < 17 and y < 17:
            dl=grid[x][y+3]*grid[x+1][y+2]*grid[x+2][y+1]*grid[x+3][y]
            dr=grid[x][y]*grid[x+1][y+1]*grid[x+2][y+2]*grid[x+3][y+3]
        cno=max(y, le, dl, dr)
        if hno < cno:
            hno=cno

print(hno)
