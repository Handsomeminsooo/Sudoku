# 백트래킹을 이용한 sudoku 풀이
import sys, time
sudoku = []
complete = 0

sudoku = [[0 for j in range(1, 10)] for i in range(9)]
for i in range(9):
    sudoku[i] = list(map(int, sys.stdin.readline().strip('\n')))
st = time.time()

def possibilities(i, j):
    global sudoku
    exist = []
    for k in range(9):
        if sudoku[k][j] != 0:
            exist.append(sudoku[k][j])
        if sudoku[i][k] != 0:
            exist.append(sudoku[i][k])
        if sudoku[i//3*3 + k//3][j//3*3 + k%3] != 0:
            exist.append(sudoku[i//3*3 + k//3][j//3*3 + k%3])
    unexist = [i for i in range(1, 10) if i not in exist]
    
    return unexist  # 리스트로 반환, 길이 0이면 가능한 수 없음

def dfs(i, j):
    global complete
    global sudoku
    if sudoku[i][j] == 0:
        pos = possibilities(i, j)
        for k in pos:
            if complete:
                return
            sudoku[i][j] = k
            #print(i, j, k)
            next_i = i
            next_j = j
            while sudoku[next_i][next_j] != 0:
                next_j += 1
                if next_j == 9:
                    next_i += 1
                    next_j = 0
                if next_i == 9:
                    for _ in range(9):
                        print(sudoku[_])
                    complete = 1
                    return  # 완성
            dfs(next_i, next_j)
        sudoku[i][j] = 0
        return
            
    next_i = i
    next_j = j
    while sudoku[next_i][next_j] != 0:
        next_j += 1
        if next_j == 9:
            next_i += 1
            next_j = 0
        if next_i == 9:
            for _ in range(9):
                print(sudoku[_])
            complete = 1
            return  # 완성
    dfs(next_i, next_j)

    return

dfs(0, 0)
print('time :', time.time() - st)