"""
SUBSETS VIA MASK
Given an integer array nums of unique elements, 
return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
The subsets can be returned in any order.
"""

class Solution(object):
    def subsets(nums):
        res = []
        n = len(nums)

        for i in range(2 ** n):
            subset = []

            for j in range(n):
                if (i >> j) & 1:
                    subset.append(nums[j])
            
            res.append(subset)
        
        return res