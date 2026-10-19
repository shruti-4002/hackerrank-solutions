# LeetCode Problem: Reverse String II
# Link: https://leetcode.com/problems/reverse-string-ii/
# Difficulty: Easy
# Language: python3

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res=[];
        for i in range(0,len(s),2*k):
            res.append(s[i:i+k][::-1]);
            res.append(s[i+k:2*k+i]);
        return "".join(res);
        