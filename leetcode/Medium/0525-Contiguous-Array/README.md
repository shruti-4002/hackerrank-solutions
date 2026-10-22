# Contiguous Array

**Difficulty:** Medium  
**Topics:** Array, Hash Table, Prefix Sum  
**LeetCode URL:** [Contiguous Array](https://leetcode.com/problems/contiguous-array/)

## Problem Description

<p>Given a binary array <code>nums</code>, return <em>the maximum length of a contiguous subarray with an equal number of </em><code>0</code><em> and </em><code>1</code>.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,0]
<strong>Output:</strong> 2
<strong>Explanation:</strong> [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1,1,1,1,0,0,0]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

## Solution

```python3
# LeetCode Problem: Contiguous Array
# Link: https://leetcode.com/problems/contiguous-array/
# Difficulty: Medium
# Language: python3

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp={0:-1};
        curr=0;
        maxi=0;

        for i in range(0,len(nums)):
            if nums[i]==0:
                curr-=1;
            else:
                curr+=1
            if curr in mp:
                #only first occ recorded 
                maxi=max(maxi,i-mp[curr]);
            else:
                 mp[curr]=i;
        return maxi; 

        
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
