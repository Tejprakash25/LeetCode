"""
322. Coin Change
You are given an integer array coins representing coins of different denominations and an integer amount representing a total
amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def coinChange(self, coins, amount):
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for x in range(1, amount + 1):
            for coin in coins:
                
                if x - coin >= 0:
                    dp[x] = min(dp[x], 1 + dp[x - coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1