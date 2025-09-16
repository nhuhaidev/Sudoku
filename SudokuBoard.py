import copy
import random
import time
class SudokuBoard:
    @staticmethod
    def timeFunction(func):
        """
        Hàm để đo thời gian thực thi của một hàm.
        """
        def wrapper(*args, **kwargs):
            startTime = time.perf_counter()
            result = func(*args, **kwargs)
            endTime = time.perf_counter()
            elapsed = endTime - startTime
            print(f"[DEBUG] Function '{func.__name__}' executed in {elapsed:.6f} seconds.")
            #  Trả cả result và elapsed_time
            return result, elapsed   
        return wrapper

    @staticmethod   
    def printBoard(board):
        """
        In bảng Sudoku ở định dạng dễ đọc.
        Thêm các dòng để phân tách các khối 3x3.
        """
        print("-" * 25)
        for i, row in enumerate(board):
            if i % 3 == 0 and i != 0:
                print("-" * 25)
            
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                
                # In số hoặc khoảnh trống cho các ô trống
                if j == 8:
                    print(num if num != 0 else "0")
                else:
                    print(str(num if num != 0 else "0") + " ", end="")
        print("-" * 25)
    @staticmethod
    def findEmptyCell(board):
        """
        Tìm ô trống đầu tiên trong bảng (giá trị là 0).
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return None
    @staticmethod
    def isValidMove(board, num, position):
        """
        Kiểm tra xem việc đặt một số vào một vị trí có hợp lệ theo quy tắc Sudoku hay không.

        """
        row, col = position

        # Kiểm tra hàng
        if num in board[row]:
            return False

        # 2. Kiểm tra cột
        for i in range(9):
            if board[i][col] == num:
                return False

        # 3. Kiểm tra khối 3x3
        # Tìm góc trên bên trái của khối 3x3
        startRow = row - row % 3
        startCol = col - col % 3

        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == num:
                    return False

        return True
    
    @staticmethod
    def countSolutions(board):
        """
        Đếm số lượng giải pháp cho một bảng Sudoku nhất định.
        Sử dụng đệ quy và quay lui để tìm tất cả các giải pháp.
        """
        emptyCell = SudokuBoard.findEmptyCell(board)
        if not emptyCell:
            return 1  # Đã tìm thấy một giải pháp hoàn chỉnh

        row, col = emptyCell
        solutionCount = 0

        for num in range(1, 10):
            if SudokuBoard.isValidMove(board, num, (row, col)):
                board[row][col] = num
                solutionCount += SudokuBoard.countSolutions(board)
                board[row][col] = 0 # Quay lui

                # Tối ưu hóa: Nếu tìm thấy nhiều hơn một giải pháp, chúng ta có thể dừng sớm.
                if solutionCount > 1:
                    return 2

        return solutionCount
