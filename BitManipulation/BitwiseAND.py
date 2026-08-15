"""
Given a range [left, right], return the bitwise AND of all numbers in this
inclusive range.
"""

class Solution(object):
    def rangeBitwiseAnd(left: int, right: int) -> int:
        shift = 0

        while left != right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift