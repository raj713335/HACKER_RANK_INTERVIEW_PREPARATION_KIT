#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    
    dictx = {}
    
    ans = []
    
    for each in queries:
        if each[0] == 1:
            if each[1] not in dictx.keys():
                dictx[each[1]] = 1
            else:
                dictx[each[1]] +=1
        elif each[0] == 2:
            if each[1] in dictx.keys():
                if dictx[each[1]] > 0:
                    dictx[each[1]] -= 1
        else:
            if each[1]>=10**6:
                ans.append(0)
            elif each[1] in dictx.values():
                ans.append(1)
            else:
                ans.append(0)
    return ans
                
                
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
