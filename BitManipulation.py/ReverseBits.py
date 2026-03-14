"""
Reverse bits of a given 32 bits unsigned integer.
"""

class Solution(object):
    def reverseBits(self, n):
        result = 0
        
        for i in range(32):
            result <<= 1
            result |= (n & 1)
            n >>= 1
        
        return result