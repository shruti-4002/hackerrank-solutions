# Spiral Matrix

**Difficulty:** Medium  
**Topics:** Array, Matrix, Simulation  
**LeetCode URL:** [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

## Problem Description

<p>Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the</em> <code>matrix</code> <em>in spiral order</em>.</p>

<p>&nbsp;</p>

## Examples

<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

## Constraints

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>

## Solution

```cpp
// LeetCode Problem: Spiral Matrix
// Link: https://leetcode.com/problems/spiral-matrix/
// Difficulty: Medium
// Language: cpp

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m= matrix[0].size();
        int n=matrix.size();

        int total=n*m;
        int c=0;

        int startrow=0;
        int startcol=0;
        int endcol=m-1;
        int endrow=n-1;
        vector<int>temp;
        while(c<total){

            //startrow=(startcol=>endcol);

            for(int i=startcol ;i<=endcol;i++){
                temp.push_back(matrix[startrow][i]);
                c++;
            }

            if(c==total)break;

            startrow++;

            //endcol=(startrow->endrow)

            for(int i=startrow ;i<=endrow;i++){
                temp.push_back(matrix[i][endcol]);
                c++;
            }

            if(c==total)break;

                endcol--;
            
            for(int i=endcol ;i>=startcol;i--){
                temp.push_back(matrix[endrow][i]);
                c++;
            }

            if(c==total)break;

                endrow--;
            
            for(int i=endrow ;i>=startrow;i--){
                temp.push_back(matrix[i][startcol]);
                c++;
            }

          
                startcol++;



        }

return temp;



    }
};
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
