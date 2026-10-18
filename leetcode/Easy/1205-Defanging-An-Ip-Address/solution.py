# LeetCode Problem: Defanging an IP Address
# Link: https://leetcode.com/problems/defanging-an-ip-address/
# Difficulty: Easy
# Language: python3

class Solution(object):
    def defangIPaddr(self, address):
        ans="";
        for x in address:
            if x=='.':
                ans+="[.]";
            else:
                ans+=x;
        return ans;

        
         
        