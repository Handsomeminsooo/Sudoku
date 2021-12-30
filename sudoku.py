# 규칙
# 0. 가정 알고리즘 전제 : 어떤 칸에 가능한 n개의 숫자들의 조합 중 정답이 적어도 1개 있다.
# (따라서 어느 칸에서 가능성이 없을 시 답이 없다고 판단. 다음 가정으로 넘어감. 
# 다음 가정이 없을 시 답 없음을 출력하고 프로그램 종료)
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

sudoku = [[] for i in range(9)]         # 정답을 저장 및 초기 입력을 받는 리스트
matrix = [[[0 for k in range(1, 10)] for j in range(9)]for i in range(9)]   # 처음에는 [[[0, 0, ..., 0], [0, 0, ..., 0], .., []], ...[[], [], ...]]으로 시작. 가능성을 체크하고 가장 많이 손대는 리스트

# 가능성 출력
def printMatrix():
    for i in range(9):
        for j in range(9):
            if type(matrix[i][j]) == list:
                word = list(map(str, matrix[i][j]))
                printword = ''.join(word)
                print('%9s' % printword, end = ' ')
            else:
                print('%9s' % matrix[i][j], end = ' ')
        print()
    return

# matrix 내 길이가 1인 리스트가 없게 해주는 함수. 매 ckeck 이후에 사용 필요. 
def confirm():
    global matrix
    for i in range(9):
        for j in range(9):
            if type(matrix[i][j]) == list and len(matrix[i][j]) == 1:
                matrix[i][j] = matrix[i][j][0]
    return
    
# 숫자를 대입하면 그 행, 그 열, 그 블록에 있는 겹치는 가능성만 제거하는 함수
def pos_check(i, j):
    global matrix
    new = matrix[i][j]
    for p in range(9):
        # 세로줄 체크
        if type(matrix[i][p]) == list:
            if new in matrix[i][p]:
                matrix[i][p].remove(new)
        # 가로줄 체크
        if type(matrix[p][i]) == list:
            if new in matrix[p][i]:
                matrix[p][i].remove(new)
    # 블록 체크
    I = i // 3
    J = j // 3
    for p in range(3):
        for q in range(3):
            if type(matrix[I * 3 + p][J * 3 + q]) == list:
                if new in matrix[I * 3 + p][J * 3 + q]:
                    matrix[I * 3 + p][J * 3 + q].remove(new)
    return

# matrix에서 추론이 완료된 칸이 있다면 스도쿠로 넘겨주는 함수 / 형식이 리스트인지 확인.
def sync():
    global sudoku
    global matrix
    for i in range(9):
        for j in range(9):
            if type(matrix[i][j]) != list and sudoku[i][j] == 0:
                sudoku[i][j] = copy.deepcopy(matrix[i][j])
    return

# 규칙을 어긴 칸이 있나 체크하는 함수   / 
def error_ckeck():
    global sudoku
    for i in range(9):
        row = []
        col = []
        block = []
        for j in range(9):      
            row.append(sudoku[j][i])
            col.append(sudoku[i][j])
            block.append(sudoku[3 * (i % 3) + j // 3][3 * (i // 3) + j % 3])
        # 한 행, 열, 블록마다 체크, 
        for k in range(1, 10):
            if row.count(k) + col.count(k) + block.count(k) !=  3:
                return 1
    return 0

# 스도쿠 풀이가 완료되었는지 체크하는 함수
def complete():
    global matrix
    for i in range(9):
        for j in range(9):
            if type(matrix[i][j]) == list:
                return 0
    
    return 1 

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
    for i in range(9):                      # 가능성 체크
        for j in range(9):
            pos_check(i, j)
            confirm()
    
    if pre_matrix == matrix:
        limit += 1
    if error_ckeck() == 1:
        print('error occured')
        for i in range(9):
            print(sudoku[i])
        break

# 3. 무작위 대입

sudoku_backup = copy.deepcopy(sudoku)
matrix_backup = copy.deepcopy(matrix)

# 한 행, 열, 블록 안에 빈 list가 있는지 검사하는 함수
def empty_check(i, j):
    global matrix
    # 세로줄 체크
    for j in range(9):
        if type(matrix[i][j]) == list:
            if len(matrix[i][j]) == 0:
                return 1
    # 가로줄 체크
    for i in range(9):
        if type(matrix[i][j]) == list:
            if len(matrix[i][j]) == 0:
                return 1
    # 블록 체크
    I = i // 3
    J = j // 3
    for p in range(3):
        for q in range(3):
            if type(matrix[I * 3 + p][J * 3 + q]) == list:
                if len(matrix[I * 3 + p][J * 3 + q]) == 0:
                    return 1
    return 0


matrix_pos_location = []
matrix_pos_num = 0
matrix_pos_index = []           ## 그 칸의 몇 번째 수까지 갔는지 기록하는 리스트    ##
possibilitiies = 1

# 가능성 칸 체크
for i in range(9):
    for j in range(9):
        if type(matrix[i][j]) == list:                      # 가능성 칸일때
            matrix_pos_location.append([j, i])              # [x, y] 형태로 저장
            matrix_pos_num += 1
            matrix_pos_index.append(0)
            possibilitiies *= len(matrix[i][j])

# while문 -> 한 경우의 수 반복, 실패하면 fail = 1이고 그 실패한 칸의 index를 1씩 증가시킴.
# index가 matrix_backup칸의 길이와 같아지면 받아올림해줌.

solution = 0
no_solution = 0                                             # 가능한 경우가 없을 경우를 체크하는 변수

if complete():                                              # 위에서 끝났는지를 확인하는 변수
    solution = 1
else:
    print('진행 상황 :')
    printMatrix()
    print('가정 시작')
    # 정보 출력
    print('possibility cells num :', len(matrix_pos_index))
    print('possibilities :', possibilitiies)


# 4.
matrix_backup = copy.deepcopy(matrix) 
while no_solution == 0 and solution == 0:                       ## 가정 반복문 ##

    cnt = 0
    fail = 0
    i = 0
    j = 0
    cell = 0
    while fail == 0 and i < 9 :    # i
        while fail == 0 and j < 9:    # j
            if type(matrix[i][j]) == list:                  # 가능성 칸 일때
                cell += 1
                if len(matrix[i][j]) == 1:                  # 길이 1인 경우 제외
                    continue          
                elif len(matrix[i][j]) == 0:                # 길이 0인 경우 -> 들어갈 수 있는 숫자가 없음 -> 실패로 간주
                    fail = 1
                    cell -= 1
                    matrix_pos_index[cell] = 0
                    if cell != 0:
                        matrix_pos_index[cell - 1] += 1
                    else:
                        no_solution = 1
                    break
                else:                                       # 나머지 경우 -> 가능성 확정
                    matrix[i][j] = matrix[i][j][matrix_pos_index[cell]]


            j += 1
        i += 1
    if fail == 1:       # 실패했을 경우
        continue
    else:
        sudoku = copy.deepcopy(matrix)
        solution = 1
        break


# 일반출력

#for i in range(9):
#    print(matrix[i])

#print('count :', cnt)

# 출력
printMatrix()