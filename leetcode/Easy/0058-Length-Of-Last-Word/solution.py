# LeetCode Problem: Length of Last Word
# Link: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy
# Language: python3

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip();
        s=s.split();
        lastindex=len(s)-1;
        c=0;

        for x in s[lastindex]:
            c+=1;
        return c;
        