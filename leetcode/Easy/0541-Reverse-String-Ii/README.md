# Reverse String II

**Difficulty:** Easy  
**Topics:** Two Pointers, String  
**LeetCode URL:** [Reverse String II](https://leetcode.com/problems/reverse-string-ii/)

## Problem Description

<p>Given a string <code>s</code> and an integer <code>k</code>, reverse the first <code>k</code> characters for every <code>2k</code> characters counting from the start of the string.</p>

<p>If there are fewer than <code>k</code> characters left, reverse all of them. If there are less than <code>2k</code> but greater than or equal to <code>k</code> characters, then reverse the first <code>k</code> characters and leave the other as original.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abcdefg", k = 2
<strong>Output:</strong> "bacdfeg"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcd", k = 2
<strong>Output:</strong> "bacd"
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>

## Solution

```python3
# LeetCode Problem: Reverse String II
# Link: https://leetcode.com/problems/reverse-string-ii/
# Difficulty: Easy
# Language: python3

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res=[];
        for i in range(0,len(s),2*k):
            res.append(s[i:i+k][::-1]);
            res.append(s[i+k:2*k+i]);
        return "".join(res);
        
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
