import sys, copy

# 9*9 이차원 배열을 출력해주는 함수
def printMap(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end = ' ')
        print()

# 빈 칸 혹은 리스트인 칸의 가능한 숫자들을 채워 주고, 바꾼 칸들의 개수를 반환하는 함수
def check_possibilities(arr):
    cnt = 0
    for i in range(9):
        for j in range(9):
            if type(arr[i][j]) == list or arr[i][j] == 0:
                pos = [k for k in range(1, 10)]
                for l in range(9):
                    if arr[l][j] in pos:        # arr[l][j] 가 arr[i][j]을 포함해도 리스트라 pos안에 없음.
                        pos.remove(arr[l][j])
                    if arr[i][l] in pos:
                        pos.remove(arr[i][l])
                    if arr[i//3 + l // 3][j//3 + l % 3] in pos:
                        pos.remove(arr[i//3 + l // 3][j//3 + l % 3])
                if arr[i][j] != pos:
                    arr[i][j] = copy.deepcopy(pos)
                    cnt += 1
    return cnt

# 행, 열, 블럭 내에서 가능한 어떤 숫자가 한 칸에만 존재할때 그 수를 확정해주는 함수
def check_onlyones(arr):
    for i in range(9):
        for j in range(9):
            if type(arr[i][j]) == list:     # 리스트 일때만 확인
                if len(arr[i][j]) == 1:     # 길이 1일때 확인
                    arr[i][j] = arr[i][j][0]
                    continue
                # 행
                others = []
                only = []
                for l in range(9):
                    if type(arr[l][j]) == list and l != i:
                        others += arr[l][j]
                only = [i for i in arr[i][j] if i not in others]
                for l in only:
                    arr[i][j] = l   ## Q : 만약 only에 값이 2개 이상 들어 있다면? A. 다른 행에는 없는 가능성이 2개 이상 존재하면 그건 오류.
                if len(only) > 1:
                    printMap(arr)   # 그 오류를 탐지하는 코드.
                
                # 열
                others = []
                only = []
                for l in range(9):
                    if type(arr[i][l]) == list and l != j:
                        others += arr[i][l]
                only = [i for i in arr[i][j] if i not in others]
                for l in only:
                    arr[i][j] = l
                if len(only) > 1:
                    printMap(arr)
                
                # 블럭
                others = []
                only = []
                for l in range(3):
                    for k in range(3):
                        if type(arr[i//3 + l][j//3 + k]) == list and not (i//3 + l == i and j//3 + k == j): # i//3 + l != i and j//3 + k != j 일때는 i, j 중 하나만 같아도 건너뜀.
                            others += arr[i//3 + l][j//3 + k]
                only = [i for i in arr[i][j] if i not in others]
                for l in only:
                    arr[i][j] = l
                if len(only) > 1:
                    printMap(arr)
    return
                

# 스도쿠 입력부
sudoku = []
for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().strip('\n'))))

while True:
    if check_possibilities(sudoku) == 0:
        break
    check_onlyones(sudoku)

printMap(sudoku)