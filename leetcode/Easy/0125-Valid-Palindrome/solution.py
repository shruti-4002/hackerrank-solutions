# LeetCode Problem: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Language: python3

class Solution:
    def isPalindrome(self, s: str) -> bool:

        start=0;
        s=" ".join(s.split());
        s=s.lower();
        end=len(s)-1;
        while start<end:
            if (s[start]).isalnum()!=True:
                start+=1;
            elif (s[end]).isalnum()!=True:
                end-=1;
            elif s[start]!=s[end]:
                return False;
            else:
                start+=1;
                end-=1;
            
        

        return True;
        
        