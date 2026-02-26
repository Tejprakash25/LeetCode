"""
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the  
"""

class Solution:
    def merge(self, intervals):
        
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            
            last_end = merged[-1][1]
            
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            
            else:
                merged.append([start, end])
            
        return merged