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

        