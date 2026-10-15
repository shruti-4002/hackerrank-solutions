# LeetCode Problem: Kids With the Greatest Number of Candies
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Difficulty: Easy
# Language: python3

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        maximum=max(candies);
        temp=[];
        for x in candies:
            if x+extraCandies>=maximum:
                temp.append(True);
            else:
                temp.append(False);
        return temp;