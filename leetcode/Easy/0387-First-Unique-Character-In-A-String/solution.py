# LeetCode Problem: First Unique Character in a String
# Link: https://leetcode.com/problems/first-unique-character-in-a-string/
# Difficulty: Easy
# Language: python3

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={};

        for x in s:
            if x not in freq:
                freq[x]=1;
            else:
                freq[x]+=1;
        
        for x in range(0,len(s)):
            if freq[s[x]]==1:
                return x;
        return -1;
        