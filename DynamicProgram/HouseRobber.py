"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can
you climb to the top?
"""

class Solution:
    def rob(self, nums):
        
        prev2 = 0
        prev1 = 0
        
        for money in nums:
            current = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current
        
        return prev1