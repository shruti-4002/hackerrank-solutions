# LeetCode Problem: Subtract the Product and Sum of Digits of an Integer
# Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Difficulty: Easy
# Language: python3

class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        sum=0;
        product=1;
        x=n;
        while(x>0):
            c=x%10;
            sum+=c;
            product*=c;
            x=x//10;
        return product-sum;

        