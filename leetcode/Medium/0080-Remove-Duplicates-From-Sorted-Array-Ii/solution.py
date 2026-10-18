# LeetCode Problem: Remove Duplicates from Sorted Array II
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Difficulty: Medium
# Language: python3

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=1;
       

        for j in range(i+1,len(nums)):
            if nums[i-1]!=nums[j]:
                i+=1;
                nums[i]=nums[j];








        return i+1;
        
        