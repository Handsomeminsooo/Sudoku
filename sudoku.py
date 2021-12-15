# 규칙
# 1. 빈칸마다 들어갈 수 있는 숫자(가능성) 작성
# 2. 한 블럭 내 그 숫자의 가능성이 1개 존재한다면 확정
# 3. 한 세로줄 내 그 가능성이 1개 존재하면 확정
# 4. 한 가로줄 내 그 가능성이 1개 존재하면 확정
# 5. 오류체크
# 6. 이전 상황이랑 같을시 찍기 시작
# 입력은 9개문자열 9줄로 입력, 빈칸은 '0'으로 입력, 

# 선언부
import sys
import copy

sudoku = [[] for i in range(9)]
matrix = [[[k for k in range(1, 10)] for j in range(9)]for i in range(9)]

# matrix 내 길이가 1인 리스트가 없게 해주는 함수. 매 ckeck 이후에 사용 필요. 
def confirm():
    global matrix
    for i in range(9):
        for j in range(9):
            if type(matrix[i][j]) == list and len(matrix[i][j]) == 1:
                matrix[i][j] = matrix[i][j][0]
    return

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

# matrix에서 추론이 완료된 칸이 있다면 스도쿠로 넘겨주는 함수
def sync():
    global sudoku
    global matrix
    for i in range(9):
        for j in range(9):
            if type(matrix[i][j]) != list and sudoku[i][j] == 0:
                sudoku[i][j] = copy.copy(matrix[i][j])
    return

# 규칙을 어긴 칸이 있나 체크하는 함수
def error_ckeck():
    global sudoku
    for i in range(9):
        answer = [i for i in range(1, 10)]
        row = []
        col = []
        block = []
        for j in range(9):
            row.append(sudoku[j][i])
            col.append(sudoku[i][j])
            block.append(sudoku[3 * (i % 3) + j // 3][3 * (i // 3) + j % 3])
        for k in range(1, 10):
            if row.count(k) + col.count(k) + block.count(k) > 3:
                return 1
    return 0

# 스도쿠 풀이가 완료되었는지 체크하는 함수
def complete():
    global matrix

# 입력부
sudoku = [[j for j in range(1, 10)] for i in range(9)]
for i in range(9):
    sudoku[i] = list(map(int, sys.stdin.readline().strip('\n')))

# 연산부

# 1. 숫자 부분 확정
for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            matrix[i][j] = sudoku[i][j]

# 2. 가능성 체크
limit = 0
cnt = 0
pre_matrix = []
while limit < 1:
    cnt += 1
    pre_matrix = copy.deepcopy(matrix)
    block_check()
    confirm()
    sync()
    row_check()
    confirm()
    sync()
    col_check()
    confirm()
    sync()
    if pre_matrix == matrix:
        limit += 1
    if error_ckeck() == 1:
        print('error occured')
        for i in range(9):
            print(sudoku[i])
        break

# 3. 무작위 대입
#while error_ckeck() == 0:
#    pass
# 출력부
#for i in range(9):
#    print(sudoku[i])
#print(sudoku)
#print()
#print(matrix)

# 일반출력

#for i in range(9):
#    print(matrix[i])

#print('count :', cnt)

# 가능성 출력
for i in range(9):
    for j in range(9):
        if type(matrix[i][j]) == list:
            word = list(map(str, matrix[i][j]))
            printword = ''.join(word)
            print('%9s' % printword, end = ' ')
        else:
            print('%9s' % matrix[i][j], end = ' ')
    print()