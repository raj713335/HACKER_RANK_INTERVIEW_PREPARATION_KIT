#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    
    max_plot = 0
    
    for k in range(0,len(h)):
        ii,jj=k,k
        for i in range(k-1,-1,-1):
            if h[i]>=h[k]:
                ii=i
            else:
                break
        for j in range(k+1,len(h)):
            if h[j]>=h[k]:
                jj=j
            else:
                break

        plot = h[k]*(jj-ii+1)

        if plot>max_plot:
            max_plot = plot
            
    return max_plot
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
