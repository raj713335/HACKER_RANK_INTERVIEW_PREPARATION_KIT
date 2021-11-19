#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    machines = sorted(machines)
    num_machines = len(machines)
    # This is the earliest day we can reach our goal if all machines = 1
    earliest_day = math.ceil(goal/num_machines)
    # Low bound number of days
    # Based on if all machines were the min machine number
    low = earliest_day * machines[0]
    # High bound number of days
    # Based on if all machines were the max machine number
    high = earliest_day * machines[-1]
    while low < high:
        # This is a guess for what day would work 
        guess_day = (low + high) // 2
        # guess_day // m gives us how many items we make for machine m
        # by guess_day
        if sum([guess_day // m for m in machines]) >= goal:
            high = guess_day
        else:
            low = guess_day + 1
    return low

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
