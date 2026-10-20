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


        