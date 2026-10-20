# LeetCode Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Language: python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq={};

        if len(s)!=len(t):
            return False;
    

        for x in s:
            if x not in freq:
                freq[x]=1;
            else:
                freq[x]+=1;
        

        for x in t:
            if x not in freq:
                return False;
            elif freq[x]<=0:
                return False
            else:
                freq[x]-=1;

        return True;

        