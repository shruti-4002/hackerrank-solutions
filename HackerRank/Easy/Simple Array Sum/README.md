# Simple Array Sum

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Simple Array Sum](https://www.hackerrank.com/challenges/simple-array-sum/problem)

## Problem Description

Given an array of integers, find the sum of its elements.

For example, if the array , , so return .

**Function Description**

Complete the  function with the following parameter(s):

* : an array of integers

**Returns**

* : the sum of the array elements

**Input Format**

The first line contains an integer, , denoting the size of the array. **
The second line contains  space-separated integers representing the array's elements.

Constraints**

**Sample Input**

```
STDIN           Function
-----           --------
6               ar[] size n = 6
1 2 3 4 10 11   ar = [1, 2, 3, 4, 10, 11]

```

**Sample Output**

```
31

```

**Explanation**

Print the sum of the array's elements: .

## Examples



## Constraints



## Solution

```python3
# HackerRank Problem: Simple Array Sum
# Link: https://www.hackerrank.com/challenges/simple-array-sum/problem
# Difficulty: Easy
# Language: python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    sum=0
    for x in ar:
        sum+=x
    return sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
