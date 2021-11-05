#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    
    include = 0
    exclude = 0
    
    for i in range(0, len(arr)):
        if include>exclude:
            exclude_new = include
        else:
            exclude_new = exclude
            
        include = arr[i] + exclude
        exclude = exclude_new
        
    return include if include>exclude else exclude
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
