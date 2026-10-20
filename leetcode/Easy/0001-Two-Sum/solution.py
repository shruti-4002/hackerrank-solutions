# LeetCode Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Language: python3

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       
       freq={};
       temp=[];

       for x in range(0,len(nums)):
        need=target-nums[x];
        if need in freq:
            temp.append(freq[need]);
            temp.append(x);
            return temp;
        else:
            freq[nums[x]]=x;
        
       return temp;
        