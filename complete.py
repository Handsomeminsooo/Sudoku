# 스도쿠가 완료되었는지 체크하는 프로그램
import sys

def complete(arr):
    lst = [i for i in range(1, 10)]
    for i in range(9):
        row = []
        col = []
        block = []
        for j in range(9):
            row.append(arr[j][i])
            col.append(arr[i][j])
            block.append(arr[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3])
        row.sort()
        col.sort()
        block.sort()
        if row != lst:
            print(i, j, 'row')
            return 0
        if col != lst:
            print(i, j, 'col')
            return 0
        if block != lst:
            print(i, j, 'block', block)
            return 0
    return 1

sudoku = []
for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().strip('\n'))))

print(complete(sudoku))