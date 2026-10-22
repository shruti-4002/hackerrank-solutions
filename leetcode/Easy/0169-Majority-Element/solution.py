# LeetCode Problem: Majority Element
# Link: https://leetcode.com/problems/majority-element/
# Difficulty: Easy
# Language: python3

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        mp={};
        for x in nums:
            if x in mp:
                mp[x]+=1;
            else:
                mp[x]=1;
        
        maxiVal=0;
        maxiCount=0;
        for keys,values in mp.items():
            if values>maxiCount:
                maxiVal=keys;
                maxiCount=values;
        return maxiVal;
        