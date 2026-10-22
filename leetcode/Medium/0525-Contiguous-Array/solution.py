# LeetCode Problem: Contiguous Array
# Link: https://leetcode.com/problems/contiguous-array/
# Difficulty: Medium
# Language: python3

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp={0:-1};
        curr=0;
        maxi=0;

        for i in range(0,len(nums)):
            if nums[i]==0:
                curr-=1;
            else:
                curr+=1
            if curr in mp:
                #only first occ recorded 
                maxi=max(maxi,i-mp[curr]);
            else:
                 mp[curr]=i;
        return maxi; 

        