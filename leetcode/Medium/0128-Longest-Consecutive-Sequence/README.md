# Longest Consecutive Sequence

**Difficulty:** Medium  
**Topics:** Array, Hash Table, Union-Find  
**LeetCode URL:** [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem Description

<p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [100,4,200,1,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,3,7,2,5,8,4,6,0,1]
<strong>Output:</strong> 9
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,2]
<strong>Output:</strong> 3
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

## Solution

```python3
# LeetCode Problem: Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium
# Language: python3

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort();

        if(len(nums)==0):
            return 0;
            
        maxi=0;
        curr=0;

        for i in range(0,len(nums)-1):
            if nums[i+1]-nums[i]==1:
                curr+=1;
                maxi=max(curr,maxi);
            elif nums[i+1]-nums[i]==0:
                continue;
            else:
                curr=0;
        return maxi+1;

        
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
