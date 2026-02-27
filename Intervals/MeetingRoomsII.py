"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        
        heap = []
        heapq.heappush(heap, intervals[0][1])
        
        for start, end in intervals[1:]:
            
            if start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
        
        return len(heap)