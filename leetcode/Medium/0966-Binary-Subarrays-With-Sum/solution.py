# LeetCode Problem: Binary Subarrays With Sum
# Link: https://leetcode.com/problems/binary-subarrays-with-sum/
# Difficulty: Medium
# Language: python3

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        mp={0:1};

        curr=0;
        count=0;

        for x in nums:
            curr+=x;
            needed=curr-goal;
            if needed in mp:
                count+=mp[needed];
            
            if curr in mp:
                mp[curr]+=1;
            else:
                mp[curr]=1;
        return count;

        