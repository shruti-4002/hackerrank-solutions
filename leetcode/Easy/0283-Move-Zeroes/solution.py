# LeetCode Problem: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy
# Language: python3

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i=-1;
        

        for j in range(0,len(nums)):
            if nums[j]!=0:
                i+=1
                nums[i],nums[j]=nums[j],nums[i];
            
            

        