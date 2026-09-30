class AI:
    def choose_position(self, board, me="O", opponent="X"):
        legal = []

        for row in range(6):
            for col in range(7):
                if board.grid[row][col] == ".":
                    legal.append((row, col))

        if not legal:
            return None

        for row, col in legal:
            test_board = self.copy_board(board)
            test_board.place(row, col, me)

            if test_board.winner(me):
                return row, col

        for row, col in legal:
            test_board = self.copy_board(board)
            test_board.place(row, col, opponent)

            if test_board.winner(opponent):
                return row, col

        return legal[0]

    def copy_board(self, board):
        from board import Board

        new_board = Board()
        new_board.grid = [row[:] for row in board.grid]

        return new_board