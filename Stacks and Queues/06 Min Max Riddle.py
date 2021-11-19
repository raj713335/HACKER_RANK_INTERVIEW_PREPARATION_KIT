#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
from collections import defaultdict
def riddle(arr):
    stack = []
    arr.append(0)
    d=defaultdict(int)
    for i,j in enumerate(arr):           #making of step 2 
        t=i
        while stack and stack[-1][0]>=j:
            val,li = stack.pop()
            d[j]=max(d[j],i-li+1)
            d[val]=max(d[val],i-li)
            t=li
        stack.append((j,t))
    #print(d)
    del d[0]
    e=defaultdict(int)
    for i in d:                           #making of step 3
        e[d[i]]=max(e[d[i]],i)
    #print(e)
    l=len(arr)
    ans=[e[l-1]]                          #at the end, "ans" is our resulted list of step 4
    for i in range(len(arr)-2,0,-1):      #making of step 4; step4: we have to add the largest value in ans(i.e. last value in ans) if the current value of e[i] is less than last value in ans, else we have to just append e[i] to ans.  
        if e[i]<ans[-1]:
            ans.append(ans[-1])
        else:
            ans.append(e[i])
    return(ans[::-1])                   #step 5: print reverse ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
