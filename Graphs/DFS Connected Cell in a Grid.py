#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def maxRegion(grid):
    # Write your code here
    visited = {}
    max_size = 0
    
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            size = exploresize(grid, r, c, visited)
            if size>max_size:
                max_size = size
                
    return max_size

def exploresize(grid, r, c, visited):
    
    if not((r >= 0) and (r < len(grid))):
        return 0
    
    if not((c >= 0) and (c < len(grid[0]))):
        return 0
    
    if grid[r][c] == 0:
        return 0
    
    pos = str(r)+","+str(c)
    
    if pos in visited.keys():
        return 0
    
    visited[pos] = True
    
    size = 1
    size += exploresize(grid, r-1, c, visited)
    size += exploresize(grid, r+1, c, visited)
    size += exploresize(grid, r, c-1, visited)
    size += exploresize(grid, r, c+1, visited)
    size += exploresize(grid, r-1, c-1, visited)
    size += exploresize(grid, r+1, c+1, visited)
    size += exploresize(grid, r-1, c+1, visited)
    size += exploresize(grid, r+1, c-1, visited)
    
    return size

    
    
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
