# sudoku_board.py
import copy

class SudokuBoard:
    """
    Đại diện cho một bảng Sudoku 9x9 và các thao tác cơ bản trên đó.
    Tên phương thức và thuộc tính theo quy ước lowerCamelCase.
    """
    def __init__(self, grid=None):
        if grid:
            self.grid = copy.deepcopy(grid)
        else:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def printBoard(self):
        """
        In bảng Sudoku ra màn hình console với định dạng dễ đọc.
        """
        print("-" * 25)
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("-" * 25)
            
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                
                cell = str(num) if num != 0 else "0"
                if j == 8:
                    print(cell)
                else:
                    print(cell + " ", end="")
        print("-" * 25)

    def findEmptyCell(self):
        """
        Tìm ô trống đầu tiên trong bảng (giá trị là 0).
        Trả về (hàng, cột) nếu tìm thấy, ngược lại trả về None.
        """
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return (row, col)
        return None

    def isValidMove(self, num, position):
        """
        Kiểm tra xem một nước đi có hợp lệ hay không.
        """
        row, col = position

        # Kiểm tra hàng
        if num in self.grid[row]:
            return False

        # Kiểm tra cột
        for i in range(9):
            if self.grid[i][col] == num:
                return False

        # Kiểm tra khối 3x3
        startRow = 3 * (row // 3)
        startCol = 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[startRow + i][startCol + j] == num:
                    return False

        return True