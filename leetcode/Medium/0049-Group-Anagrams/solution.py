# LeetCode Problem: Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Language: python3

class Solution:
    def groupAnagrams(self, s: list[str]) -> list[list[str]]:
        temp=[];
        freq={};

        for x in s:
            arr= sorted(x);
            arr="".join(arr);
            if arr not in freq:
                freq[arr]=[];
            freq[arr].append(x);
        
        for key,values in freq.items():
            temp.append(values);
        
        return temp;
         

                
        