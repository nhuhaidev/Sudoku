from SudokuBoard import SudokuBoard

class SudokuSolver:
    @staticmethod
    def solveSudoku(board):
        emptyCell = SudokuBoard.findEmptyCell(board)
        if not emptyCell:
            return True
        row, col = emptyCell
        for num in range(1, 10):
            if SudokuBoard.isValidMove(board, num, (row, col)):
                board[row][col] = num
                
                if SudokuSolver.solveSudoku(board):
                    return True
                board[row][col] = 0
        return False

