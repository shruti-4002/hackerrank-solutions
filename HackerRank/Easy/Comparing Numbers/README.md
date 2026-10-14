# Comparing Numbers

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Comparing Numbers](https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem)

## Problem Description

Given two integers,  and , identify whether  or  or .

Exactly one of the following lines: **
- *X is less than Y*

- *X is greater than Y*

- *X is equal to Y*

Input Format**

Two lines containing one integer each ( and , respectively).

**Constraints**

-

**Output Format**

Exactly one of the following lines: **
- *X is less than Y*

- *X is greater than Y*

- *X is equal to Y*

Sample Input**

**Sample Input 1**

```
5
2

```

**Sample Input 2**

```
2
2

```

**Sample Input 3**

```
2
3

```

**Sample Output**

**Sample Output 1**

```
X is greater than Y

```

**Sample Output 2**

```
X is equal to Y

```

**Sample Output 3**

```
X is less than Y

```

**Explanation**

-

## Examples



## Constraints



## Solution

```bash
# HackerRank Problem: Comparing Numbers
# Link: https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem
# Difficulty: Easy
# Language: bash

read num1
read num2

if(($num1>$num2))
then
echo "X is greater than Y"
fi

if(($num1<$num2))
then
echo "X is less than Y"
fi

if(($num1==$num2))
then
echo "X is equal to Y"
fi

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
