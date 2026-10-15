# Subtract the Product and Sum of Digits of an Integer

**Difficulty:** Easy  
**Topics:** Math  
**LeetCode URL:** [Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)

## Problem Description

Given an integer number <code>n</code>, return the difference between the product of its digits and the sum of its digits.
<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 234
<strong>Output:</strong> 15 
<b>Explanation:</b> 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4421
<strong>Output:</strong> 21
<b>Explanation: 
</b>Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
</ul>

## Solution

```python3
# LeetCode Problem: Subtract the Product and Sum of Digits of an Integer
# Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Difficulty: Easy
# Language: python3

class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        sum=0;
        product=1;
        x=n;
        while(x>0):
            c=x%10;
            sum+=c;
            product*=c;
            x=x//10;
        return product-sum;

        
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
