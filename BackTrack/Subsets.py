"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. The subsets can be returned in any order.
"""

class Solution:
    def subsets(self, nums):

        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result