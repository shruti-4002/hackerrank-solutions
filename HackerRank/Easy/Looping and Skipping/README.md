# Looping and Skipping

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Looping and Skipping](https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem)

## Problem Description

Your task is to use *for* loops to display only *odd* natural numbers from  to .

**Input Format**

*There is no input.*

**Constraints**

-

**Output Format**

```
1
3
5
.
.
.
.
.
99

```

**Sample Input**

-

**Sample Output**

```
1
3
5
.
.
.
.
.
99

```

**Explanation**

-

## Examples



## Constraints



## Solution

```bash
# HackerRank Problem: Looping and Skipping
# Link: https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem
# Difficulty: Easy
# Language: bash

for((i=1;i<100;i++))
    do
    if((i%2!=0))
       then
     echo $i;
     fi
    
    done

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
