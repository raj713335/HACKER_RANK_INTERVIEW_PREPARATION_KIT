#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    
    dictx = {}
    
    a=sorted(a)
    b=sorted(b)
    
  
    x=0
    
    for i in range(len(a)):
        if a[i] not in dictx.keys():
            dictx[a[i]]=1
        else:
            dictx[a[i]]+=1
    for i in range(len(b)):        
        if b[i] not in dictx.keys():
            dictx[b[i]]=-1
        else:
            dictx[b[i]]-=1
            
    for each in dictx.values():
        x+=abs(each)
        
        
    return(x)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
