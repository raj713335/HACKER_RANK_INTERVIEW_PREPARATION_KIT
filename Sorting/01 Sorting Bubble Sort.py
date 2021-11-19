#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    
    count = 0
    
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
                count += 1
                
    print("Array is sorted in {} swaps.".format(count))
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[-1]))
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
