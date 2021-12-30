# 임시로 만들어 줌
matrix = []
sudoku = []

# 블록, 행, 열에서 가능한 유일한 숫자가 있나 체크하는 함수
def block_check():
    global sudoku       # **전역 변수 사용 설정
    global matrix
    for i in range(9):  # 블럭 마다
        exist = []
        for j in range(9):
            I = 3 * (i % 3) + j // 3
            J = 3 * (i // 3) + j % 3
            cell = sudoku[I][J]
            if cell != 0 and cell not in exist: # 블럭 내 존재하는 수들의 리스트 생성
                exist.append(cell)

        for j in range(9):
            I = 3 * (i % 3) + j // 3            # ** i, j 재선언 필요. 그렇지 않으면 이전 for문에서의 값 계속 사용. for문에서도 지역변수 형태로 존재하는듯.
            J = 3 * (i // 3) + j % 3
            if type(matrix[I][J]) == list:      # 가능성이 여러 개 있으면 -> matrix 요소에서 리스트 형태로 존재. 길이 1인 리스트 지우기 위해 comfirm 필요함.
                for k in exist:
                    if k in matrix[I][J]:
                        matrix[I][J].remove(k)
    return

def row_check():
    global sudoku
    global matrix
    for i in range(9):  # 행 마다
        exist = []
        for j in range(9):
            cell = sudoku[j][i]
            if cell != 0 and cell not in exist:
                exist.append(cell)

        for j in range(9):
            if type(matrix[j][i]) == list:
                for k in exist:
                    if k in matrix[j][i]:
                        matrix[j][i].remove(k)
    return

def col_check():
    global sudoku
    global matrix
    for i in range(9):  # 열 마다
        exist = []
        for j in range(9):
            cell = sudoku[i][j]
            if cell != 0 and cell not in exist:
                exist.append(cell)

        for j in range(9):
            if type(matrix[i][j]) == list:
                for k in exist:
                    if k in matrix[i][j]:
                        matrix[i][j].remove(k)
    return