from typing import List, Optional, Tuple


def print_board(board: List[List[int]]) -> None:
    '''Print a sudoku board'''
    for i in range(9):
        print(" ".join(map(str, board[i])))

def find_empty_spot(board: List[List[int]]) -> Optional[Tuple[int, int]]:
    '''Find an empty spot (denoted with a 0) in a sudoku board'''
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid(board: List[List[int]], new_num: int, position: Tuple[int, int]) -> bool:
    '''Check if given number and position are valid for the board'''
    # position[0] is the row, position[1] is the column
    if new_num not in range(1, 10):
        raise ValueError(f"illegal number: {new_num}")
    # check that there are no duplicates in the row
    if new_num in (board[position[0]][x] for x in range(9)):
        return False
    # check that there are no duplicates in the column
    if new_num in (board[x][position[1]] for x in range(9)):
        return False
    # check that there are no duplicates in the sub-grid
    box_row = position[0] // 3 * 3
    box_col = position[1] // 3 * 3
    if new_num in (board[i][j]
                   for i in range(box_row, box_row+3)
                   for j in range(box_col, box_col+3)):
        return False
    return True

def solve(board: List[List[int]]) -> bool:
    '''Solve sudoku board in-place if solvable'''
    empty_spot = find_empty_spot(board)
    while empty_spot is not None:
        for num in range(1, 10):
            # check if current number is a possible solution
            if is_valid(board, num, empty_spot):
                board[empty_spot[0]][empty_spot[1]] = num

                # recurse
                if solve(board):
                    break

                # reset if solution is no longer valid
                board[empty_spot[0]][empty_spot[1]] = 0
        else:
            # board state is invalid
            return False
        empty_spot = find_empty_spot(board)
    return True

def find_and_print_solution(board: List[List[int]]) -> None:
    '''Attempt to solve sudoku board and print completed board'''
    if solve(board):
        print_board(board)
    else:
        print('no solution exists')
