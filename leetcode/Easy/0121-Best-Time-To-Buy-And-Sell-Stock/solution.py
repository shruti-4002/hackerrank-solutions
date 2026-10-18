# LeetCode Problem: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Language: python3

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=prices[0];
        profit=0;

        for sell in range(1,len(prices)):
            currprofit=prices[sell]-buy;
            profit=max(profit,currprofit);
            buy=min(buy,prices[sell]);
        return profit;
            
        