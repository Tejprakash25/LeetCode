"""LeetCode 372: Super Pow."""

from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        modulus = 1337
        result = 1

        for digit in b:
            result = self._pow_mod(result, 10, modulus)
            result = result * self._pow_mod(a, digit, modulus) % modulus

        return result

    @staticmethod
    def _pow_mod(base: int, exponent: int, modulus: int) -> int:
        result = 1
        base %= modulus

        while exponent > 0:
            if exponent & 1:
                result = result * base % modulus

            base = base * base % modulus
            exponent >>= 1

        return result