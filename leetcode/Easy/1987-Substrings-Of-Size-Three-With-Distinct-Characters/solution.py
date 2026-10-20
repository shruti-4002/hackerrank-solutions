# LeetCode Problem: Substrings of Size Three with Distinct Characters
# Link: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
# Difficulty: Easy
# Language: python3

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0;
        for i in range(0,len(s)-2):
            
            temp=set();

            for x in range(0,3):
                temp.add(s[i+x]);
            if len(temp)==3:
                c+=1;
        return c;
    
        