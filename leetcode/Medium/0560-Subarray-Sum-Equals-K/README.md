# Subarray Sum Equals K

**Difficulty:** Medium  
**Topics:** Array, Hash Table, Prefix Sum  
**LeetCode URL:** [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

## Problem Description

<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the total number of subarrays whose sum equals to</em> <code>k</code>.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1], k = 2
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3], k = 3
<strong>Output:</strong> 2
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>7</sup> &lt;= k &lt;= 10<sup>7</sup></code></li>
</ul>

## Solution

```python3
# LeetCode Problem: Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Difficulty: Medium
# Language: python3

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={};
        count=0;
        mp[0]=1;
        curr=0
        for x in nums:
            curr+=x;
            needed=curr-k;
            if needed in mp:
                count+=mp[needed];
                
            if curr in mp:
                mp[curr]+=1;
            else:
                mp[curr]=1;
        return count;
        
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
