# Unique Paths

**Difficulty:** Medium  
**Topics:** Math, Dynamic Programming, Combinatorics  
**LeetCode URL:** [Unique Paths](https://leetcode.com/problems/unique-paths/)

## Problem Description

<p>There is a robot on an <code>m x n</code> grid. The robot is initially located at the <strong>top-left corner</strong> (i.e., <code>grid[0][0]</code>). The robot tries to move to the <strong>bottom-right corner</strong> (i.e., <code>grid[m - 1][n - 1]</code>). The robot can only move either down or right at any point in time.</p>

<p>Given the two integers <code>m</code> and <code>n</code>, return <em>the number of possible unique paths that the robot can take to reach the bottom-right corner</em>.</p>

<p>The test cases are generated so that the answer will be less than or equal to <code>2 * 10<sup>9</sup></code>.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px;" />
<pre>
<strong>Input:</strong> m = 3, n = 7
<strong>Output:</strong> 28
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> m = 3, n = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right
3. Down -&gt; Right -&gt; Down
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
</ul>

## Solution

```python3
# LeetCode Problem: Unique Paths
# Link: https://leetcode.com/problems/unique-paths/
# Difficulty: Medium
# Language: python3

class Solution:

    def fun(self,i:int,j:int,m:int,n:int,dp:list[list[int]])->int:
        if i<0 or j<0 or i>=m or j>=n:
            return 0;
        
        if i==m-1 and j==n-1:
            return 1;

        if dp[i][j]!=-1:
            return dp[i][j];

        down=self.fun(i+1,j,m,n,dp);
        right=self.fun(i,j+1,m,n,dp);

        dp[i][j]=down+right;
        return dp[i][j]


    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for i in range(n)] for j in range(m)]
        c=self.fun(0,0,m,n,dp);
        return c;


        
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
