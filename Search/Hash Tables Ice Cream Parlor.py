#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    
    dictx = {}
    
    for i in range(0,len(cost)):
        dictx[cost[i]] = (i+1)
        
    for i in range(0, len(cost)):
        temp = money-cost[i]
        if temp==cost[i]:
            if cost.count(temp)<2:
                continue
                
        if temp in dictx.keys():
            return (sorted([i+1,dictx[temp]]))
    
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        print(*whatFlavors(cost, money))
        
        
