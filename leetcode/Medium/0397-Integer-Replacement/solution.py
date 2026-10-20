# LeetCode Problem: Integer Replacement
# Link: https://leetcode.com/problems/integer-replacement/
# Difficulty: Medium
# Language: python3

class Solution:
    def integerReplacement(self, n: int) -> int:
        c=0;

        while n!=1:
            if n%2==0:
                n=n//2;
                c+=1;
            elif n==3 or n%4==1:
                n=n-1;
                c+=1;
            else:
                n=n+1;
                c+=1;
        return c;
    

        