# LeetCode Problem: Next Greater Element I
# Link: https://leetcode.com/problems/next-greater-element-i/
# Difficulty: Easy
# Language: python3

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq={};
        stack=[];
        ans=[];
        stack.append(nums2[len(nums2)-1]);
        freq[nums2[len(nums2)-1]]=-1;

        for i in range(len(nums2)-2,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop();

            if len(stack)==0:
                freq[nums2[i]]=-1;
            else:
                freq[nums2[i]]=stack[-1];

            stack.append(nums2[i]);
            
        for x in nums1:

            ans.append(freq[x]);
        return ans;
      