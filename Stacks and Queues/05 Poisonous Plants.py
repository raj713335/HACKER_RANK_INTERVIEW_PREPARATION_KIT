#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    # Write your code here
    stack = []
    maxDays = -math.inf

    for plant in p:
        days = 1

        while stack and stack[-1][0] >= plant:
            _, d = stack.pop()
            days = max(days, d + 1)
        
        if not stack:
            days = 0
        
        maxDays = max(maxDays, days)
        stack.append((plant, days))
    
    return maxDays

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
