#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#



"""
Let's begin:
1.  Bribing the person in front of you is the only way to go forward. Take note of this point.
2.  Instances of numbers greater than you in front of you = Bribe count
3.  Do we really have to check everyone in our front?

First, to eliminate the chaotic cases - obviously any person who is more than 2 positions ahead of their initial 
position cannot be there since they could not have bribed more than twice.


Question to ask yourself: How can I know how many times have I been bribed if I am the one standing in the queue?
Every person with a number greater than me who is now standing ahead of me must have bribed me at some point.
So starting from one position in front of you, check through the row in front of you and count the instances of 
numbers greater than yours. Hence, Instances of numbers greater than you in front of you = Bribe count.

Final step, notice the inner loop for this condition starts from j=i-2 (1 position in front of you) and goes 
to either 0 (beginning of queue) or your original position - 1 i.e q[i-1]-2 : whichever is maximum of the two.
Why?

1 2 3 4 5 6 7 8 9 10
1 2 3 5 6 7 8 9 10 4 : 6 bribes
1 2 5 3 6 7 8 9 10 4 : 7 bribes
1 5 2 3 6 7 8 9 10 4 : 8 bribes BUT 5 has now bribed three people - 4,3,2 so this won't happen.
So you only needed to check till one position in front of you.

That will be in this instance q[3] - 2 = 4 -2 = 2 (indexing starting from 0, initial position of 4 is 3)

void minimumBribes(vector<int> q) {
    int bribes=0;
    for(int i=q.size();i>=1;--i)
    { 
        if (q[i - 1] - i > 2) {
          cout << "Too chaotic\n";
          return;
        }
        //Check to front of my position, if there are numbers greater than me then they must have bribed me to get ahead.
    for(int j=i-2;j>=max(q[i-1]-2,0);--j)
    if(q[j]>q[i-1]) bribes++;       
    }
     cout<<bribes<<"\n";  
}

"""

def minimumBribes(q):
    # Write your code here
    count = 0

    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return 0
        for j in range(max(0, q[i] - 2),i):
            if (q[j] > q[i]):
                count += 1

    print(count)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
