# LeetCode Problem: Intersection of Two Arrays
# Link: https://leetcode.com/problems/intersection-of-two-arrays/
# Difficulty: Easy
# Language: python3

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

            temp=set();

            for x in nums1:
                if x in nums2:
                    temp.add(x);
            return list(temp);
        