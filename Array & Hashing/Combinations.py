class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(start):
            if len(path) == k:
                result.append(path.copy())
                return

            remaining = k - len(path)

            for num in range(start, n - remaining + 2):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
        return result