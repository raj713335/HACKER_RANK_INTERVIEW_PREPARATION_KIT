#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_dict = {}
    count_sock_pairs = 0

    for each in ar:
        if each not in sock_dict.keys():
            sock_dict[each] = 1
        else:
            sock_dict[each] += 1

    for each in sock_dict.values():
        count_sock_pairs += int(each / 2)

    return count_sock_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()