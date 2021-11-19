#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def stepPerms(n):
    f1, f2, f3 = 1, 2, 4
    for i in range(n-1):
        f1, f2, f3 = f2, f3, f1 + f2 + f3
    return f1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
