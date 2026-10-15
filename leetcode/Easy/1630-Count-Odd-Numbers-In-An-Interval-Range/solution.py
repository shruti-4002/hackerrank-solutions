# LeetCode Problem: Count Odd Numbers in an Interval Range
# Link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# Difficulty: Easy
# Language: python3

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low=low-1
        odd_num_till_low=(low+1)//2
        odd_num_till_high=(high+1)//2;
        return odd_num_till_high-odd_num_till_low;
        