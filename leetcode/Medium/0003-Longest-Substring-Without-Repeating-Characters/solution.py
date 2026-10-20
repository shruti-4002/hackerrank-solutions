# LeetCode Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Language: python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxi=0;
        if not s:
            return 0;

        if len(s)==1:
            return 1;
      

        temp=set();
        i=0;
        temp.add(s[i]);
        for j in range(1,len(s)):

            if s[j] not in temp:
                temp.add(s[j]);
               
                maxi=max(j-i+1,maxi);
            else:
                while(s[j] in temp):
                   
                    temp.remove(s[i])
                    i+=1;
                    
                temp.add(s[j]);  
                maxi=max(j-i+1,maxi);

             

        return maxi;
        