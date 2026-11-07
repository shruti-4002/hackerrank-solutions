# LeetCode Problem: Missing Number
# Link: https://leetcode.com/problems/missing-number/
# Difficulty: Easy
# Language: python3

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort();
        i=0;
        for x in nums:
            if i!=x:
                return i;
            else:
                i+=1;

        return len(nums);
        