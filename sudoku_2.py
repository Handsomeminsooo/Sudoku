import sys, copy

# 16*16 이차원 배열을 출력해주는 함수
def printMap(arr):
    for i in range(16):
        for j in range(16):
            if type(arr[i][j]) == list:
                temp = list(map(str, arr[i][j]))
                print('[%16s]' % ''.join(temp), end = ' ')
            else:
                print('%11d' % arr[i][j], end = ' ')
        print()

# 입력에 알맞은 모양으로 16*16 이차원 배열을 출력하는 함수
def justPrint(arr):
    for i in range(16):
        for j in range(16):
            print(arr[i][j], end = '')
        print()
    return

# 보기 쉽도록 한 블록씩 떼서 출력하는 함수
def easyPrint(arr):
    for i in range(16):
        if i % 4 == 0 and i != 0:
            print()
        for j in range(16):
            if j % 4 == 0 and j != 0:
                print(' ', end = '  ')
            print(arr[i][j], end = '')
        
        print()
    return

# 빈 칸 혹은 리스트인 칸의 가능한 숫자들을 채워 주고, 바꾼 칸들의 개수를 반환하는 함수
def check_possibilities(arr):
    cnt = 0
    for i in range(16):
        for j in range(16):
            if type(arr[i][j]) == list or arr[i][j] == 0:
                pos = [k for k in range(1, 10)]
                for l in range(16):
                    if arr[l][j] in pos:        # arr[l][j] 가 arr[i][j]을 포함해도 리스트라 pos안에 없음.
                        #print(pos, end = ' ')
                        pos.remove(arr[l][j])
                        #print('>', pos, 'row')
                    if arr[i][l] in pos:
                        #print(pos, end = ' ')
                        pos.remove(arr[i][l])
                        #print('>', pos, 'col')
                    if arr[i//4 * 4 + l // 4][j//4 * 4 + l % 4] in pos:
                        #print(pos, end = ' ')
                        pos.remove(arr[i//4 * 4 + l // 4][j//4 * 4 + l % 4])    # MISTAKE : 3으로 정수 나눗셈 후 다시 3 곱해 줘야함.
                        #print('>', pos, 'block')
                if arr[i][j] != pos or arr[i][j] == 0:
                    arr[i][j] = copy.deepcopy(pos)
                    cnt += 1
            #printMap(sudoku)
    return cnt

# 행, 열, 블럭 내에서 가능한 어떤 숫자가 한 칸에만 존재할때 그 수를 확정해주는 함수
def check_onlyones(arr):
    for i in range(16):
        for j in range(16):
            if type(arr[i][j]) == list:     # 리스트 일때만 확인
                #print()
                #print('check', i, j, arr[i][j])
                if len(arr[i][j]) == 1:     # 길이 1일때 확인
                    #print(i, j, arr[i][j], end = ' ')
                    arr[i][j] = arr[i][j][0]
                    #print('>', arr[i][j])
                    
                    return
                
                # 행
                others = []
                only = []
                for l in range(16):
                    if type(arr[l][j]) == list and l != i:
                        others += arr[l][j]
                only = [l for l in arr[i][j] if l not in others]
                
                if len(only) > 1:
                    print('error in row', i, j, only)
                    print(type(arr[i][j]), arr[i][j])
                    printMap(arr)   # 그 오류를 탐지하는 코드.

                for l in only:
                    #print(i, j, arr[i][j], end = ' ')
                    arr[i][j] = l   ## Q : 만약 only에 값이 2개 이상 들어 있다면? A. 다른 행에는 없는 가능성이 2개 이상 존재하면 그건 오류.
                    #print('>', arr[i][j])
                    return          ## ** 확정해주면 다시 돌아가서 가능성 제거 해줘야함.

                # 열
                others = []
                only = []
                for l in range(16):
                    if type(arr[i][l]) == list and l != j:
                        others += arr[i][l]
                only = [l for l in arr[i][j] if l not in others]

                if len(only) > 1:
                    print('error in col', i, j, only)
                    print(type(arr[i][j]), arr[i][j])
                    printMap(arr)
                
                for l in only:
                    #print(i, j, arr[i][j], end = ' ')
                    arr[i][j] = l
                    #print('>', arr[i][j])
                    return
            

                # 블럭
                others = []
                only = []
                for l in range(4):
                    for k in range(4):
                        if type(arr[i//4 * 4 + l][j//4 * 4 + k]) == list and not (i//4 * 4 + l == i and j//4 * 4 + k == j): # i//4 + l != i and j//4 + k != j 일때는 i, j 중 하나만 같아도 건너뜀.
                            others += arr[i//4 * 4+ l][j//4 * 4 + k]
                only = [l for l in arr[i][j] if l not in others]
                
                if len(only) > 1:
                    print('error in block', i, j, only)
                    print(type(arr[i][j]), arr[i][j])
                    printMap(arr)

                for l in only:
                    #print(i, j, arr[i][j], end = ' ')
                    arr[i][j] = l
                    #print('>', arr[i][j])
                    return
                
    return
                

# 스도쿠 입력부
sudoku = []
for i in range(16):
    sudoku.append(list(map(int, sys.stdin.readline().strip('\n'))))

while True:
    sudoku_backup = copy.deepcopy(sudoku)
    check_possibilities(sudoku)
    check_onlyones(sudoku)
    if sudoku == sudoku_backup: # 바뀐 것이 없을 때 반복 마침.
        break

printMap(sudoku)
justPrint(sudoku)
easyPrint(sudoku)
