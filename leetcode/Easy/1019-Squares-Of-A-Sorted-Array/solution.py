# LeetCode Problem: Squares of a Sorted Array
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# Difficulty: Easy
# Language: python3

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        for i in range(0,len(nums)):
            nums[i]=nums[i]*nums[i];

        nums.sort()
        return nums;

        