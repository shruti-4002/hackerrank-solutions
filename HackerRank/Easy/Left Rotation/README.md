# Left Rotation

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Left Rotation](https://www.hackerrank.com/challenges/array-left-rotation/problem)

## Problem Description

A  operation on a circular array shifts each of the array's elements  unit to the left. The elements that fall off the left end reappear at the right end. Given an integer , rotate the array that many steps to the left and return the result.

**Example** **

After  rotations, .

Function Description**

Complete the  function with the following parameters:

* : the amount to rotate by

* : the array to rotate

**Returns**

* : the rotated array

**Input Format**

The first line contains two space-separated integers that denote , the number of integers, and , the number of left rotations to perform. **
The second line contains  space-separated integers that describe .

Constraints**

*

*

*

**Sample Input**

```
STDIN      Function
-----      --------
5 4         n = 5 d = 4
1 2 3 4 5  arr = [1, 2, 3, 4, 5]

```

**Sample Output**

```
5 1 2 3 4

```

**Explanation**

To perform  left rotations, the array undergoes the following sequence of changes:

## Examples



## Constraints



## Solution

```python3
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

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
