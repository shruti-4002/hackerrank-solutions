# LeetCode Problem: Reverse Words in a String
# Link: https://leetcode.com/problems/reverse-words-in-a-string/
# Difficulty: Medium
# Language: python3

class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split();
        s.reverse();
        return " ".join(s);
        