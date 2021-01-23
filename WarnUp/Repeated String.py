#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
      
    total_number_of_full_string=math.floor(n/len(s))
    length_of_partial_string=n-(len(s)*total_number_of_full_string)
    count_a=(s.count('a')*total_number_of_full_string)+s[:length_of_partial_string].count('a')
    
    return(count_a)
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()