"""
494. Target Sum
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before
2 and a '-' before 1 and concatenate them to build the expression "+2-1".
"""

class Solution:
    def findTargetSumWays(self, nums, target):

        total = sum(nums)

        if (target + total) % 2 != 0 or abs(target) > total:
            return 0

        subset = (target + total) // 2

        dp = [0] * (subset + 1)
        dp[0] = 1

        for num in nums:
            for s in range(subset, num-1, -1):
                dp[s] += dp[s-num]

        return dp[subset]