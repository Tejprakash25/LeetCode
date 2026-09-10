class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    value = board[r][c]
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[(r // 3) * 3 + (c // 3)].add(value)

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] != ".":
                        continue

                    box = (r // 3) * 3 + (c // 3)

                    for value in "123456789":
                        if (value not in rows[r] and
                            value not in cols[c] and
                            value not in boxes[box]):

                            board[r][c] = value
                            rows[r].add(value)
                            cols[c].add(value)
                            boxes[box].add(value)

                            if backtrack():
                                return True

                            board[r][c] = "."
                            rows[r].remove(value)
                            cols[c].remove(value)
                            boxes[box].remove(value)

                    return False

            return True

        backtrack()