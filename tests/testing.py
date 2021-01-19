import sys
from solver.solver import SudokuSolver
import unittest

#not solvable r5c1 has no valid values
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

class SudokuTest(unittest.TestCase):
    def setUp(self):
        self.sudokuSolver = SudokuSolver()

    def test_find_empty_spot(self):
        self.sudokuSolver.print_board(invalid_board)
        self.assertEqual(self.sudokuSolver.find_empty_spot(invalid_board), (0, 0))
        self.assertEqual(self.sudokuSolver.find_empty_spot(valid_board), (0, 1))

    def test_is_valid(self):
        self.assertFalse(self.sudokuSolver.is_valid(invalid_board, 2, (0, 0)))
        self.assertFalse(self.sudokuSolver.is_valid(invalid_board, 6, (0, 0)))
        self.assertTrue(self.sudokuSolver.is_valid(invalid_board, 1, (0, 0)))
        self.assertFalse(self.sudokuSolver.is_valid(valid_board, 8, (1, 2)))
        #self.assertTrue(self.sudokuSolver.is_valid(valid_board))
