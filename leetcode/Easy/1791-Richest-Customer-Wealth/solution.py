# LeetCode Problem: Richest Customer Wealth
# Link: https://leetcode.com/problems/richest-customer-wealth/
# Difficulty: Easy
# Language: python3

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        ans=0;

        for acc in accounts:

            Sum=0;
            for j in acc:
                Sum+=j;
            ans=max(Sum,ans);
        return ans;

        