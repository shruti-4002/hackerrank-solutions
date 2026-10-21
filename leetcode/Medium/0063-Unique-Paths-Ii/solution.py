# LeetCode Problem: Unique Paths II
# Link: https://leetcode.com/problems/unique-paths-ii/
# Difficulty: Medium
# Language: python3

class Solution:

    def fun(self,i:int,j:int,m:int,n:int,dp:list[list[int]],g:list[list[int]])->int:
        if i<0 or j<0 or i>=m or j>=n:
            return 0;
        
        if i==m-1 and j==n-1:
            return 1;
        
        if g[i][j]==1:
            return 0;

        if dp[i][j]!=-1:
            return dp[i][j];

        down=self.fun(i+1,j,m,n,dp,g)
        right=self.fun(i,j+1,m,n,dp,g);

        dp[i][j]=right+down;

        return dp[i][j];






    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        
        if obstacleGrid[m-1][n-1]==1:
            return 0;

        dp=[[-1 for i in range(n)] for j in range(m) ];
        return  self.fun(0,0,m,n,dp,obstacleGrid);

        
        