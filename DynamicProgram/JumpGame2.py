"""
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps. You can assume that you can always reach the last index.
"""

class Solution:
    def jump(self, nums):

        jumps = 0
        l = r = 0

        while r < len(nums) - 1:

            farthest = 0

            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            jumps += 1

        return jumps