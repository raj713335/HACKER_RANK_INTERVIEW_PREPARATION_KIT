#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    count = 0
    iter = 1
    while iter!=len(s):
        for i in range(0,len(s)-1):
            for j in range(i+1,len(s)-iter+11):
                if sorted(s[i:i+iter]) == sorted(s[j:j+iter]):   
                    count+=1
                    
        iter += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
