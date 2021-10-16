#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    
    dictx = {}
    count = 0

    for each in arr:
        if each not in dictx.keys():
            dictx[each] = 1
        else:
            dictx[each] += 1

    print(dictx)

    for each in arr:
        i, j = 0, 0
        if (each * r) in dictx.keys():
            i = dictx[each * r]
        if (each * r * r) in dictx.keys():
            j = dictx[each * r * r]

        if min(i, j) > 0:
            count += (((i-1) * (j-1)))

        dictx[each] -= 1

    return count
             
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
