#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the triplets function below.
def triplets(a, b, c):
    
    a = sorted(set(a))
    b = sorted(set(b), reverse=True)
    c = sorted(set(c))
    
    
    count = 0
    
    
    
    for i in range(0, len(b)):
        aa = bisect.bisect(a, b[i])
        cc = bisect.bisect(c, b[i])
        count += (aa*cc)
                        
    return count
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
