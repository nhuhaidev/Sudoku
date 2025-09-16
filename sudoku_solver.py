# sudoku_solver.py
from sudoku_board import SudokuBoard

def solveSudoku(boardObj):
    """
    Giải bảng Sudoku bằng thuật toán backtracking đệ quy.
    """
    emptyCell = boardObj.findEmptyCell()
    if not emptyCell:
        return True

    row, col = emptyCell
    for num in range(1, 10):
        if boardObj.isValidMove(num, (row, col)):
            boardObj.grid[row][col] = num

            if solveSudoku(boardObj):
                return True

            boardObj.grid[row][col] = 0
            
    return False

def countSolutions(boardObj):
    """
    Đếm số lượng lời giải có thể có cho một bảng Sudoku.
    """
    emptyCell = boardObj.findEmptyCell()
    if not emptyCell:
        return 1

    row, col = emptyCell
    solutionCount = 0

    for num in range(1, 10):
        if boardObj.isValidMove(num, (row, col)):
            boardObj.grid[row][col] = num
            solutionCount += countSolutions(boardObj)
            boardObj.grid[row][col] = 0

            if solutionCount > 1:
                return 2

    return solutionCount