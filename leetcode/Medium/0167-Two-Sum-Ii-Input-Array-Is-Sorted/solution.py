# LeetCode Problem: Two Sum II - Input Array Is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Difficulty: Medium
# Language: python3

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq={};
        temp=[];
        for x in range(0,len(nums)):
            need=target-nums[x];
            if need in freq:
                temp.append(freq[need]);
                temp.append(x+1);
                return temp;
            else:
                freq[nums[x]]=x+1;
        return temp;
        
        