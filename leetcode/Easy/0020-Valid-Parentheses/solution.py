# LeetCode Problem: Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Language: python3

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[];
        mp={')':"(","}":"{","]":"["};
        for k in s:
            if  k=='(' or k=='[' or k=='{':
                stack.append(k);
            else:
                if stack and mp[k]==stack[-1]:
                    stack.pop();
                else:
                    return False;
                    

                    
          
        
        if stack:
            return False;
        else:
            return True;
           
   

        
        