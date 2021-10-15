#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    
    dictx = {}
    
    for each in note:
        if each not in dictx.keys():
            dictx[each] = 1
        else:
            dictx[each] += 1
    #print(dictx)
            
    for each in magazine:
        if each in dictx.keys():
            dictx[each] -= 1
            
    #print(dictx)
    
    for each in dictx.values():
        if each>0:
            return "No"
        
    return "Yes"

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
