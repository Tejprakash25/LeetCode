"""Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list is even
there is no middle value and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3. For arr = [2,3], the median is (2 + 3) / 2"""

import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   
        self.large = []   

    def addNum(self, num):
        
        heapq.heappush(self.small, -num)
        
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        return (-self.small[0] + self.large[0]) / 2.0