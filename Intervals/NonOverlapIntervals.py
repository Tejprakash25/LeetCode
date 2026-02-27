"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals):
        
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        
        remove = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            
            start, end = intervals[i]
            
            if start < prev_end:
                remove += 1
            else:
                prev_end = end
        
        return remove