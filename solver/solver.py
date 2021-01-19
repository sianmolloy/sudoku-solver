#what do I need?
# -setup tests or atleast on like board of data to run the program with
# -need to determine what makes a valid solution, and a partial/potential valid solution
# -then need to solve for valid solution using backtracking
# algorithm: add next safe number recursively

class SudokuSolver:
    def is_valid(x):
        #a number is a valid addition if:
        # 1. it is not present in that row,
        # 2. it is not present in that column,
        # 3. it is not present in the 3x3 sub-grid around it
        return x + 1;

    def main():
        pass
        #call solve
        #print result (failure or success, etc)
