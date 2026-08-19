class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        if i < n and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Read digits
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        # 32-bit integer range
        return max(-2**31, min(num, 2**31 - 1))