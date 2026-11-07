# LeetCode Problem: Missing Number
# Link: https://leetcode.com/problems/missing-number/
# Difficulty: Easy
# Language: python3

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sum1=sum(nums);
        n=len(nums);
        sum2=(n*(n+1))//2;
        return sum2-sum1;

        