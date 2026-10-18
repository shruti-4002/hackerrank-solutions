# LeetCode Problem: Sort Array By Parity
# Link: https://leetcode.com/problems/sort-array-by-parity/
# Difficulty: Easy
# Language: python3

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i=0;

        for j in range(0,len(nums)):
            if nums[j]%2==0:
                nums[i],nums[j]=nums[j],nums[i];
                i+=1
        return nums;
            

        