# Integer Replacement

**Difficulty:** Medium  
**Topics:** Dynamic Programming, Greedy, Bit Manipulation, Memoization  
**LeetCode URL:** [Integer Replacement](https://leetcode.com/problems/integer-replacement/)

## Problem Description

<p>Given a positive integer <code>n</code>,&nbsp;you can apply one of the following&nbsp;operations:</p>

<ol>
	<li>If <code>n</code> is even, replace <code>n</code> with <code>n / 2</code>.</li>
	<li>If <code>n</code> is odd, replace <code>n</code> with either <code>n + 1</code> or <code>n - 1</code>.</li>
</ol>

<p>Return <em>the minimum number of operations needed for</em> <code>n</code> <em>to become</em> <code>1</code>.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 8
<strong>Output:</strong> 3
<strong>Explanation:</strong> 8 -&gt; 4 -&gt; 2 -&gt; 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> 4
<strong>Explanation: </strong>7 -&gt; 8 -&gt; 4 -&gt; 2 -&gt; 1
or 7 -&gt; 6 -&gt; 3 -&gt; 2 -&gt; 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 2
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

## Solution

```python3
# LeetCode Problem: Integer Replacement
# Link: https://leetcode.com/problems/integer-replacement/
# Difficulty: Medium
# Language: python3

class Solution:
    def integerReplacement(self, n: int) -> int:
        c=0;

        while n!=1:
            if n%2==0:
                n=n//2;
                c+=1;
            elif n==3 or n%4==1:
                n=n-1;
                c+=1;
            else:
                n=n+1;
                c+=1;
        return c;
    

        
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
