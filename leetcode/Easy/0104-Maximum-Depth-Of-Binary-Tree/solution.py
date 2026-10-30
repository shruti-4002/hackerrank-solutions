# LeetCode Problem: Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy
# Language: python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def fun(curr):
            if curr==None:
                return 0;
            
            left=fun(curr.left);
            right=fun(curr.right);

            return max(left,right)+1;

        return fun(root);

        