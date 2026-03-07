"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums):

        maxReach = 0

        for i in range(len(nums)):

            if i > maxReach:
                return False

            maxReach = max(maxReach, i + nums[i])

        return True