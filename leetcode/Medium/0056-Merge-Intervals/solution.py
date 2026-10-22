# LeetCode Problem: Merge Intervals
# Link: https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium
# Language: python3

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0]);

        temp=[];
        temp.append(intervals[0]);

        for x in range(1,len(intervals)):
            if temp[-1][1]>=intervals[x][0] :
                temp[-1][1]=max(intervals[x][1],temp[-1][1]);
            else:
                temp.append(intervals[x]);
        return temp;

        
        