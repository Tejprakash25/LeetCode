"""
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start
in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
The test cases are generated so that the answer will be less than or equal to 2 *
"""

class Solution:
    def uniquePaths(self, m, n):

        dp = [1]*n

        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c-1]

        return dp[-1]