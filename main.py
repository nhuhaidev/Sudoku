from shutil import copy
import random
from SudokuSolver import SudokuSolver   
from SudokuBoard import SudokuBoard
from SudokuGenerator import SudokuGenerator
import copy
if __name__ == "__main__":
    print("--- Sudoku Generator and Solver ---")
    
    #puzzleDifficulty = random.randint(40, 60)
    puzzleDifficulty = 60
    puzzle = SudokuGenerator.createPuzzle(puzzleDifficulty)

    print("\n[+] Randomly generated puzzle:")
    SudokuBoard.printBoard(puzzle)
with open("SudokuResult.txt", "a") as f:
    f.write("-" * 25 + "\n")
    for i, row in enumerate(puzzle):
        if i % 3 == 0 and i != 0:
            f.write("-" * 25 + "\n")

        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                f.write("| ")

            cell = str(num if num != 0 else "0")
            if j == 8:
                f.write(cell + "\n")  
            else:
                f.write(cell + " ")
    f.write("-" * 25 + "\n")
    print("\n[+] Searching for the solution...")
    solutionBoard = copy.deepcopy(puzzle)

    solved, elapsed_time = SudokuBoard.timeFunction(SudokuSolver.solveSudoku)(solutionBoard)

    if solved:
        print("\n[+] Solution found:")
        SudokuBoard.printBoard(solutionBoard)
    else:
        print("\n[!] No solution found for this puzzle.")

with open("SudokuResult.txt", "a") as f:
    f.write("-" * 25 + "\n")
    for i, row in enumerate(solutionBoard):
        if i % 3 == 0 and i != 0:
            f.write("-" * 25 + "\n")

        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                f.write("| ")

            cell = str(num if num != 0 else "0")
            if j == 8:
                f.write(cell + "\n")  
            else:
                f.write(cell + " ")
    f.write("-" * 25 + "\n")
    f.write(f"\n New Puzzle Difficulty: {puzzleDifficulty} \n")
    f.write(f"\nSolved in {elapsed_time:.6f} seconds\n")

    f.write("-" * 40 + "\n")
