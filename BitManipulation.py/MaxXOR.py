"""
Given an array of numbers, find the maximum XOR of any two numbers in the 
array.
"""

class Solution(object):
    def findMaximumXOR(self, nums):
        max_xor = 0  

        for i in range(31, -1, -1):
            max_xor <<= 1

            prefixes = set(num >> i for num in nums)

            desire = max_xor | 1

            if any((desire ^ p) in prefixes for p in prefixes):
                max_xor = desire
              
        return max_xor