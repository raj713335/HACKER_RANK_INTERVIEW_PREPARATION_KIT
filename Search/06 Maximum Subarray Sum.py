#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    # Write your code here
    
    mm,pr=0,0
    a1=[]
    for i in a:
        pr=(pr+i)%m
        mm=max(mm,pr)
        ind=bisect.bisect_left(a1,pr+1)
        if(ind<len(a1)):
            mm=max(mm,pr-a1[ind]+m)
        bisect.insort(a1,pr)
    return mm

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
