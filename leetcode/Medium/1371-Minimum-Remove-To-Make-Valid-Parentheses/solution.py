# LeetCode Problem: Minimum Remove to Make Valid Parentheses
# Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Difficulty: Medium
# Language: python3

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[];
        ans="";
        
        for i in range(0,len(s)):
            if s[i].isalpha():
                continue;
            else:
                if s[i]=='(':
                    stack.append(i);
                elif s[i]==')':
                    if stack and s[stack[-1]]=='(':
                        stack.pop();
                    else:
                        stack.append(i);

        for i in range(0,len(s)):
            if i in stack:
                continue;
            else:
                ans+=s[i];

        return ans;




        