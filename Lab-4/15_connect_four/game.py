from board import Board
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("Connect Four — you are X.")

        while True:
            self.board.print()

            if self.turn == "X":

                raw_row = input("Row (1-6), or q: ").strip().lower()

                if raw_row == "q":
                    print("Game ended.")
                    return

                try:
                    row = int(raw_row) - 1
                except ValueError:
                    print("Invalid row. Enter a number from 1 to 6.")
                    continue

                if not 0 <= row < 6:
                    print("Invalid row. Choose a row from 1 to 6.")
                    continue

                raw_col = input("Column (1-7): ").strip()

                try:
                    col = int(raw_col) - 1
                except ValueError:
                    print("Invalid column. Enter a number from 1 to 7.")
                    continue

                if not 0 <= col < 7:
                    print("Invalid column. Choose a column from 1 to 7.")
                    continue

            else:
                position = self.ai.choose_position(self.board)

                if position is None:
                    self.board.print()
                    print("Draw.")
                    return

                row, col = position

                print(
                    f"AI chooses row {row + 1}, "
                    f"column {col + 1}."
                )

            success = self.board.place(row, col, self.turn)

            if not success:
                print(
                    "That position is unavailable. "
                    "Choose an empty position."
                )
                continue


            print(
                f"{self.turn} placed a disc at "
                f"row {row + 1}, column {col + 1}."
            )

            if self.board.winner(self.turn):
                self.board.print()
                print(self.turn, "wins!")
                return

            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            self.turn = "O" if self.turn == "X" else "X"