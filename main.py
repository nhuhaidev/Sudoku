# main.py
import random
import time
from sudoku_board import SudokuBoard
from sudoku_generator import generatePuzzle
from sudoku_solver import solveSudoku

def timeFunction(func):
    """Decorator để đo thời gian thực thi của một hàm."""
    def wrapper(*args, **kwargs):
        startTime = time.perf_counter()
        result = func(*args, **kwargs)
        endTime = time.perf_counter()
        elapsed = endTime - startTime
        print(f"[DEBUG] '{func.__name__}' thực thi trong {elapsed:.6f} giây.")
        return result, elapsed
    return wrapper

def saveBoardToFile(boardObj, fileHandle, title):
    """Ghi một bảng Sudoku vào file."""
    fileHandle.write(f"--- {title} ---\n")
    for i, row in enumerate(boardObj.grid):
        if i % 3 == 0 and i != 0:
            fileHandle.write("-" * 21 + "\n")
        
        line = []
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                line.append("|")
            line.append(str(num) if num != 0 else "0")
        
        fileHandle.write(" ".join(line) + "\n")
    fileHandle.write("-" * 21 + "\n")

def main():
    """Hàm chính điều khiển luồng của chương trình."""
    print("--- Trình tạo và giải Sudoku ---")

    # difficulty = random.randint(40, 60)
    difficulty = 60
    print(f"\n[+] Đang tạo câu đố với độ khó (số ô trống): {difficulty}")
    puzzleBoard = generatePuzzle(difficulty)
    elapsedTime = timeFunction(solveSudoku)(puzzleBoard)
    print("\n[+] Câu đố đã được tạo ngẫu nhiên:")
    puzzleBoard.printBoard()

    print("\n[+] Đang tìm kiếm lời giải...")
    solutionBoard = SudokuBoard(puzzleBoard.grid)

    solved, elapsedTime = timeFunction(solveSudoku)(solutionBoard)

    if solved:
        print("\n[+] Tìm thấy lời giải:")
        solutionBoard.printBoard()
    else:
        print("\n[!] Không tìm thấy lời giải cho câu đố này.")

    try:
        with open("SudokuResult.txt", "a", encoding="utf-8") as f:
            f.write("\n" + "="*40 + "\n")
            f.write(f"Độ khó mới: {difficulty}\n")
            saveBoardToFile(puzzleBoard, f, "Câu đố")
            f.write("\n")
            if solved:
                saveBoardToFile(solutionBoard, f, "Lời giải")
                f.write(f"Giải trong {elapsedTime:.6f} giây\n")
            else:
                f.write("Không có lời giải.\n")
            f.write("="*40 + "\n")
        print("\n[+] Câu đố và lời giải đã được lưu vào file 'SudokuResult.txt'")
    except IOError as e:
        print(f"\n[!] Lỗi khi ghi file: {e}")

if __name__ == "__main__":
    main()