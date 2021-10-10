#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    
    dictx = {}
    
    flag = True
    prev = -1
    
    for i in range(0, len(s)):
        if s[i] not in dictx.keys():
            dictx[s[i]] = 1
        else:
            dictx[s[i]] += 1
            
            
    print(dictx)
            
    values = list(set(dictx.values()))
    val = list(dictx.values())
    
    
    if len(values) == 1:
        return "YES"
    elif len(values) == 2:
        if val.count(values[0])>1 and val.count(values[1])>1:
            return "NO"
        else:
            values = sorted(values)
            if (values[0] == (values[1]-1)):
                return "YES"
            elif (values[0]-1) == 0 and (val.count(values[0])) == 1:               
                return "YES"
            elif (values[1]-1) == 0 and (val.count(values[1])) == 1:               
                return "YES"
            else:
                return "NO"
    else:
        return "NO"
            
             
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
