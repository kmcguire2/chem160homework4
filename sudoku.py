from sudoku_class import *

mysudoku = sudoku()
        
for i in range(30, 71, 5):
    completed = 0
    for j in range(50):
        mysudoku.makepuzzle(i)
        mysudoku.solve()
        if mysudoku.solved() == 1:
            completed += 1
    print("%d %5.2f"%(i, completed/50))
