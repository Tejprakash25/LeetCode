"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

class Solution:
    def permute(self, nums):
        
        result = []
        used = [False] * len(nums)
        
        def backtrack(path):
            
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                
                if used[i]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                
                backtrack(path)
                
                path.pop()
                used[i] = False
        
        backtrack([])
        return result