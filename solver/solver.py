

class SudokuSolver:

    def print_board(self, board):
        print()
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" ")
            print()

    def find_empty_spot(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None

    # determine if a new number is valid (i.e. doesn't violate any rules)
    # rules:
    # 1. it isn't already in that row,
    # 2. it isn't already in that column,
    # 3. it isn't already in that 3x3 sub-grid
    def is_valid(self, board, new_num, position):
        # position[0] is the row of the new num
        # position[1] is the column of the new num
        assert new_num in range(1, 10), f"illegal number: {new_num}"
        for i in range(9):
            if board[position[0]][i] == new_num:
                return False
        for i in range(9):
            if board[i][position[1]] == new_num:
                return False
        box_row = position[0] // 3 * 3
        box_col = position[1] // 3 * 3
        for i in range(box_row, box_row+3):
            for j in range(box_col, box_col+3):
                if board[i][j] == new_num:
                    return False
        return True


    def solve(self, board):
        #if no empty spots return true
        empty_spot = self.find_empty_spot(board)
        while empty_spot is not None:
            for num in range(1, 10):
                #print(f'valid check: num {num}, spot: {empty_spot}, result:  {self.is_valid(board, num, empty_spot)}')
                if self.is_valid(board, num, empty_spot):
                    board[empty_spot[0]][empty_spot[1]] = num

                    if self.solve(board):
                        break

                    board[empty_spot[0]][empty_spot[1]] = 0
            else:
                return False
            empty_spot = self.find_empty_spot(board)
        return True


    def main(self, board):
        self.solve(board)
        self.print_board(board)
