import copy
import random
import time
class SudokuBoard:
    @staticmethod
    def timeFunction(func):
    
        def wrapper(*args, **kwargs):
            startTime = time.perf_counter()
            result = func(*args, **kwargs)
            endTime = time.perf_counter()
            elapsed = endTime - startTime
            print(f"Function '{func.__name__}' executed in {elapsed:.6f} seconds.")
        
            return result, elapsed   
        return wrapper

    @staticmethod   
    def printBoard(board):
       
        print("-" * 25)
        for i, row in enumerate(board):
            if i % 3 == 0 and i != 0:
                print("-" * 25)
            
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                
                
                if j == 8:
                    print(num if num != 0 else "0")
                else:
                    print(str(num if num != 0 else "0") + " ", end="")
        print("-" * 25)
    @staticmethod
    def findEmptyCell(board):
       
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return None
    @staticmethod
    def isValidMove(board, num, position):
      
        row, col = position

      
        if num in board[row]:
            return False

   
        for i in range(9):
            if board[i][col] == num:
                return False

       
        startRow = row - row % 3
        startCol = col - col % 3

        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == num:
                    return False

        return True
    
    @staticmethod
    def countSolutions(board):
        
        emptyCell = SudokuBoard.findEmptyCell(board)
        if not emptyCell:
            return 1 

        row, col = emptyCell
        solutionCount = 0

        for num in range(1, 10):
            if SudokuBoard.isValidMove(board, num, (row, col)):
                board[row][col] = num
                solutionCount += SudokuBoard.countSolutions(board)
                board[row][col] = 0 

             
                if solutionCount > 1:
                    return 2

        return solutionCount

