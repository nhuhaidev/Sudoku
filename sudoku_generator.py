# sudoku_generator.py
import random
from sudoku_board import SudokuBoard
from sudoku_solver import solveSudoku, countSolutions

def _fillFullBoard(boardObj):
    """Hàm nội bộ để điền đầy một bảng Sudoku một cách ngẫu nhiên."""
    emptyCell = boardObj.findEmptyCell()
    if not emptyCell:
        return True
    
    row, col = emptyCell
    numberList = list(range(1, 10))
    random.shuffle(numberList)

    for num in numberList:
        if boardObj.isValidMove(num, (row, col)):
            boardObj.grid[row][col] = num
            if _fillFullBoard(boardObj):
                return True
            boardObj.grid[row][col] = 0
    return False

def generatePuzzle(difficulty):
    """
    Tạo ra một câu đố Sudoku mới với một lời giải duy nhất.
    """
    board = SudokuBoard()
    _fillFullBoard(board)

    cells = list(range(81))
    random.shuffle(cells)
    
    removedCells = 0
    for cellIndex in cells:
        if removedCells >= difficulty:
            break
            
        row = cellIndex // 9
        col = cellIndex % 9
        
        backupValue = board.grid[row][col]
        board.grid[row][col] = 0

        boardCopy = SudokuBoard(board.grid)

        if countSolutions(boardCopy) != 1:
            board.grid[row][col] = backupValue
        else:
            removedCells += 1
            
    return board