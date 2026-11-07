# LeetCode Problem: Rotate Array
# Link: https://leetcode.com/problems/rotate-array/
# Difficulty: Medium
# Language: python3

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k=k%len(nums);

        nums.reverse();
        nums[0:k]=nums[0:k][::-1];
        nums[k:]=nums[k:][::-1]


        
        