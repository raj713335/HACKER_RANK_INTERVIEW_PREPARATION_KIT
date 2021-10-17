#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    
    arr = sorted(expenditure[:d])
    count = 0
    
    for i in range(d, len(expenditure)):
        if d%2==0:
            temp = (arr[d//2]+arr[(d//2)-1])/2
        else:
            temp = arr[d//2]
        if temp*2 <= expenditure[i]:
            count += 1
        bisect.insort(arr, expenditure[i])

        del arr[bisect.bisect_left(arr, expenditure[i-d])]
        
    return count
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
