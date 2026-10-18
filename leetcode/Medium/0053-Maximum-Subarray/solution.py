# LeetCode Problem: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium
# Language: python3

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr=nums[0];
        maxi=curr;

        for j in range(1,len(nums)):
            curr=max(curr+nums[j],nums[j]);
            maxi=max(curr,maxi);
        return maxi;

        