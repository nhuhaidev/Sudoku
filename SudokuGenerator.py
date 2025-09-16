
import random
from SudokuBoard import SudokuBoard
import copy

class SudokuGenerator:
    
    def createPuzzle(difficulty):
   
        # 1. Tạo một bảng trống
        board = [[0 for _ in range(9)] for _ in range(9)]

        # 2. Tạo một giải pháp hoàn chỉnh ngẫu nhiên
        def fillFullBoard(emptyBoard):
            emptyCell = SudokuBoard.findEmptyCell(emptyBoard)
            if not emptyCell:
                return True
            row, col = emptyCell
            
            numberList = list(range(1, 10))
            random.shuffle(numberList) # Nguồn ngẫu nhiên chính

            for num in numberList:
                if SudokuBoard.isValidMove(emptyBoard, num, (row, col)):
                    emptyBoard[row][col] = num
                    if fillFullBoard(emptyBoard):
                        return True
                    emptyBoard[row][col] = 0
            return False

        fillFullBoard(board)

        # 3. Tạo lỗ trong bảng trong khi đảm bảo có một giải pháp duy nhất
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

            # Tạo một bản sao để kiểm tra giải pháp duy nhất
            boardCopy = copy.deepcopy(board)

            if SudokuBoard.countSolutions(boardCopy) != 1:
                # Nếu giải pháp không duy nhất, khôi phục giá trị
                board[row][col] = backupValue
            else:
                removedCells += 1
        return board