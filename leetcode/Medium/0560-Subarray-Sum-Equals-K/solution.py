# LeetCode Problem: Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Difficulty: Medium
# Language: python3

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={};
        count=0;
        mp[0]=1;
        curr=0
        for x in nums:
            curr+=x;
            needed=curr-k;
            if needed in mp:
                count+=mp[needed];
                
            if curr in mp:
                mp[curr]+=1;
            else:
                mp[curr]=1;
        return count;
        