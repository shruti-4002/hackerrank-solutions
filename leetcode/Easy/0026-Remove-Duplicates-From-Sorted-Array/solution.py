# LeetCode Problem: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Language: python3

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

       i=0;
       
       for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1;
            nums[i]=nums[j];
       return i+1;




        