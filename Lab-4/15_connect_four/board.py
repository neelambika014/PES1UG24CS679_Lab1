ROWS, COLS = 6, 7


class Board:
    def __init__(self):
        self.grid = [["."] * COLS for _ in range(ROWS)]

    def place(self, row, col, token):
        if not 0 <= row < ROWS:
            return False

        if not 0 <= col < COLS:
            return False

        if self.grid[row][col] != ".":
            return False

        self.grid[row][col] = token
        return True

    def full(self):
        return all(
            self.grid[r][c] != "."
            for r in range(ROWS)
            for c in range(COLS)
        )

    def winner(self, token):
        directions = [
            (0, 1),    
            (1, 0),   
            (1, 1),    
            (1, -1)    
        ]

        for r in range(ROWS):
            for c in range(COLS):
                if self.grid[r][c] != token:
                    continue

                for dr, dc in directions:
                    if all(
                        0 <= r + i * dr < ROWS
                        and 0 <= c + i * dc < COLS
                        and self.grid[r + i * dr][c + i * dc] == token
                        for i in range(4)
                    ):
                        return True

        return False

    def print(self):
        print("\n  " + " ".join(str(i + 1) for i in range(COLS)))

        for i, row in enumerate(self.grid):
            print(str(i + 1) + " " + " ".join(row))