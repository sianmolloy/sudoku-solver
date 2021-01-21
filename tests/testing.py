import sys
import solver.solver as solver
import unittest

# not solvable r5c1 has no valid values
invalid_board = [
    [0, 0, 9, 0, 2, 8, 7, 0, 0],
    [8, 0, 6, 0, 0, 4, 0, 0, 5],
    [0, 0, 3, 0, 0, 0, 0, 0, 4],
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 7, 1, 3, 4, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [3, 0, 0, 0, 0, 0, 5, 0, 0],
    [9, 0, 0, 4, 0, 0, 8, 0, 7],
    [0, 0, 1, 2, 5, 0, 3, 0, 0]
]
valid_board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]
almost_solved_valid_board = [
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 4, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 3, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 9, 4, 7, 2, 5, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 2, 0, 6, 3, 0, 0],
]

class SudokuTest(unittest.TestCase):

    def test_print_board(self):
        solver.print_board(valid_board)
        solver.print_board(invalid_board)

    def test_find_empty_spot(self):
        self.assertEqual(solver.find_empty_spot(invalid_board), (0, 0))
        self.assertEqual(solver.find_empty_spot(valid_board), (0, 1))
        self.assertEqual(solver.find_empty_spot(almost_solved_valid_board), (8, 4))

    def test_is_valid(self):
        self.assertFalse(solver.is_valid(invalid_board, 2, (0, 0)))
        self.assertFalse(solver.is_valid(invalid_board, 6, (0, 0)))
        self.assertTrue(solver.is_valid(invalid_board, 1, (0, 0)))
        self.assertFalse(solver.is_valid(valid_board, 8, (1, 2)))
        self.assertTrue(solver.is_valid(valid_board, 1, (1, 2)))
        self.assertTrue(solver.is_valid(valid_board, 1, (0, 1)))
        self.assertTrue(solver.is_valid(almost_solved_valid_board, 8, (8, 4)))

    def test_is_valid_input_validation(self):
        with self.assertRaises(ValueError):
            solver.is_valid(valid_board, 0, (1, 2))
        with self.assertRaises(ValueError):
            solver.is_valid(valid_board, 10, (1, 2))

    def test_solve(self):
        self.assertTrue(solver.solve(almost_solved_valid_board))
        self.assertTrue(solver.solve(valid_board))
        self.assertFalse(solver.solve(invalid_board))

    def test_main(self):
        solver.find_and_print_solution(almost_solved_valid_board)
        solver.find_and_print_solution(valid_board)
        solver.find_and_print_solution(invalid_board)
