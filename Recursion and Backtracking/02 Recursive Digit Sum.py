#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    
    s=str(sum([int(i) for i in n]))
    
    if len(n) == 1:
        if k == 1:
            return n
        else:
            return superDigit(n * k, 1)
    else:
        return(superDigit(s,k))
        
    
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    s=superDigit(n, k)
    print(s)
    


