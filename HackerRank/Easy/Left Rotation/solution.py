# HackerRank Problem: Left Rotation
# Link: https://www.hackerrank.com/challenges/array-left-rotation/problem
# Difficulty: Easy
# Language: python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def reverse(num,start,end):

    while(start<end):
        num[start],num[end]=num[end],num[start]
        start+=1
        end-=1

def rotateLeft(k, num):
    n=len(num)
    k=k%n
    reverse(num,0,k-1)
    reverse(num,k,len(num)-1)
    reverse(num,0,len(num)-1)
    return num
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
