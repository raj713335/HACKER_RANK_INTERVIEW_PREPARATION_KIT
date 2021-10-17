#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    
    stack = [s[0]]
    dictx = {"(": ")","{":"}","[":"]"}

    
    for i in range(1, len(s)):
        if len(stack) != 0 and stack[-1] in dictx.keys() and dictx[stack[-1]] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
            
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
