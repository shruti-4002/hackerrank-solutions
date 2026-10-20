# LeetCode Problem: Next Greater Element II
# Link: https://leetcode.com/problems/next-greater-element-ii/
# Difficulty: Medium
# Language: python3

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:

        stack=[];
        ans=[];

        arr_len=len(nums);

        for i in range(arr_len-1,-1,-1):
            stack.append(nums[i]);

        for i in range(arr_len-1,-1,-1):
            while stack and  stack[-1]<=nums[i]:
                stack.pop();

            if len(stack)==0:
                ans.append(-1);
            else:
                ans.append(stack[-1]);

            stack.append(nums[i]);
        
        ans.reverse();
        return ans;
        