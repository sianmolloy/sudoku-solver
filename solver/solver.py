

class SudokuSolver:

    def print_board(self, board):
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
        for i in range(9):
            if board[position[0]][i] == new_num:
                return False
        for i in range(9):
            if board[i][position[0]] == new_num:
                return False
        box_row = position[0] // 3 * 3
        box_col = position[0] // 3 * 3
        for i in range(box_row, box_row+3):
            for j in range(box_row, box_row+3):
                if board[i][j] == new_num:
                    return False
        return True


    def solve():
        pass

    def main():
        pass
        #call solve
        #print result (failure or success, etc)
