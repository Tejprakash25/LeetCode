"""
152. Maximum Product Subarray
Given an integer array nums, find a contiguous non-empty subarray within the array that has the
largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
"""

class Solution:
    def maxProduct(self, nums):
        
        curMax = nums[0]
        curMin = nums[0]
        result = nums[0]
        
        for n in nums[1:]:
            
            tempMax = max(n, n * curMax, n * curMin)
            curMin = min(n, n * curMax, n * curMin)
            curMax = tempMax
            
            result = max(result, curMax)
        
        return result