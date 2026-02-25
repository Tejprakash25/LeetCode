"""
215. Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element."""

import random

class Solution:
    def findKthLargest(self, nums, k):
        
        k = len(nums) - k
        
        def quickselect(l, r):
            pivot = nums[random.randint(l, r)]
            p = l
            
            for i in range(l, r + 1):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            if k < p - 1:
                return quickselect(l, p - 2)
            elif k > p - 1:
                return quickselect(p, r)
            else:
                return nums[p - 1]
        
        return quickselect(0, len(nums) - 1)