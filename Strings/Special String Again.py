#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = 1
    list = []
    curr = s[0]

    ans = 0

    for i in range(1, len(s)):
        if s[i] == curr:
            count += 1
        else:
            list.append([curr, count])
            curr = s[i]
            count = 1
    list.append([s[i], count])


    for each in list:
        ans += (each[1]*(each[1]+1))//2

    for i in range(1,len(list)-1):
        if list[i-1][0]==list[i+1][0] and list[i][1]==1:
            ans += min(list[i-1][1], list[i+1][1])
            
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
