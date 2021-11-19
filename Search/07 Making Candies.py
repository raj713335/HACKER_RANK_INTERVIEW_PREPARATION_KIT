#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m, w, p, n):
    # Write your code here
    candy = 0
    invest = 0
    spend = sys.maxsize
    while candy < n:
        passes = (p - candy) // (m * w)
        if passes <= 0:
            mw = (candy // p) + m + w
            half = math.ceil(mw / 2)
            if m > w:
                m = max(m, half)
                w = mw - m
            else:
                w = max(w, half)
                m = mw - w
            candy %= p
            passes = 1
        candy += passes * m * w
        invest += passes
        spend = min(spend, invest + math.ceil((n - candy) / (m * w)))
    return min(invest, spend)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
