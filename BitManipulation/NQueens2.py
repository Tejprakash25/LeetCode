class Solution:
    def totalNQueens(self, n: int) -> int:
        full = (1 << n) - 1

        def backtrack(cols, diag, anti_diag):
            if cols == full:
                return 1

            count = 0

            available = full & ~(cols | diag | anti_diag)

            while available:
                bit = available & -available
                available -= bit

                count += backtrack(
                    cols | bit,
                    (diag | bit) << 1 & full,
                    (anti_diag | bit) >> 1
                )

            return count

        return backtrack(0, 0, 0)