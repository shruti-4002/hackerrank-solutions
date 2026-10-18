# LeetCode Problem: Defanging an IP Address
# Link: https://leetcode.com/problems/defanging-an-ip-address/
# Difficulty: Easy
# Language: python

class Solution(object):
    def defangIPaddr(self, address):
          return address.replace(".","[.]");
        