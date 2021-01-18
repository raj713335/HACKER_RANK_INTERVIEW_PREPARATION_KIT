#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    position,jumps=0,0
    
    while position+1<len(c):
        try:
            if c[position+2]!=1 and c[position+1]!=1:
                position+=2
            elif c[position+2]!=1 and c[position+1]==1:
                position+=2
            elif c[position+2]==1 and c[position+1]!=1:
                position+=1
        except:
            if c[position+1]!=1:
                position+=1
        
                
            
        jumps+=1
    
    return(jumps)
                    
    
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()