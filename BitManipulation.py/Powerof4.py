"""
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n ==
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n <= 0:
            return False

        if (n & (n-1)) != 0:
            return False
        
        return (n & 0x55555555) != 0