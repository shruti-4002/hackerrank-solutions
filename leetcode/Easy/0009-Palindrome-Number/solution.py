# LeetCode Problem: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Language: python3

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0;
        num=x;
        while(num>0):
            c=num%10;
            rev=rev*10+c;
            num=num//10;
        if rev==x:
            return True;
        else:
            return False;