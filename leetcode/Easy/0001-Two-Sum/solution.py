# LeetCode Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Language: python3

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq={};
        for i in range(0,len(nums)):
            need=target-nums[i];
            if need in freq:
                return [freq[need],i];
            
            freq[nums[i]]=i;



        
        