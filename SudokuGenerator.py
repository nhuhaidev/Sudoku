
import random
from SudokuBoard import SudokuBoard
import copy

class SudokuGenerator:
    
    def createPuzzle(difficulty):
   
      
        board = [[0 for _ in range(9)] for _ in range(9)]

      
        def fillFullBoard(emptyBoard):
            emptyCell = SudokuBoard.findEmptyCell(emptyBoard)
            if not emptyCell:
                return True
            row, col = emptyCell
            
            numberList = list(range(1, 10))
            random.shuffle(numberList) 

            for num in numberList:
                if SudokuBoard.isValidMove(emptyBoard, num, (row, col)):
                    emptyBoard[row][col] = num
                    if fillFullBoard(emptyBoard):
                        return True
                    emptyBoard[row][col] = 0
            return False

        fillFullBoard(board)

        
        cells = list(range(81))
        random.shuffle(cells)
        
        removedCells = 0
        for cellIndex in cells:
            if removedCells >= difficulty:
                break
                
            row = cellIndex // 9
            col = cellIndex % 9
            
            backupValue = board[row][col]
            board[row][col] = 0

          
            boardCopy = copy.deepcopy(board)

            if SudokuBoard.countSolutions(boardCopy) != 1:
                
                board[row][col] = backupValue
            else:
                removedCells += 1

        return board
