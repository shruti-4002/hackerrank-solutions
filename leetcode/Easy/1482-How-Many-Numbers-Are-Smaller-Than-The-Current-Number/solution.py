# LeetCode Problem: How Many Numbers Are Smaller Than the Current Number
# Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Difficulty: Easy
# Language: python3

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        temp=[]
        for i in range(0,len(nums)):
            count=0;
            for j in range(0,len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            temp.append(count);
        return temp;
        