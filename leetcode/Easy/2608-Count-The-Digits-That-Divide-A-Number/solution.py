# LeetCode Problem: Count the Digits That Divide a Number
# Link: https://leetcode.com/problems/count-the-digits-that-divide-a-number/
# Difficulty: Easy
# Language: python3

class Solution:
    def countDigits(self, num: int) -> int:
        c=num;
        count=0;
        while(c>0):
            k=c%10;
            if num%k==0:
                count+=1
            c=c//10;
        return count;