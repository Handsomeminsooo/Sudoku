# 함수 설명
printMatrix - matrix를 출력해 주는 함수

confirm - 길이가 1인 리스트를 확정해주는 함수

* only_check - 그 행, 열, 블록에 한 개만 존재하는 가능성을 확정하는 함수, confirm 과는 다른 점이 confirm 은 가능성이 1일때만 확정, 이건 행, 열, 블록 단위로 조사.
* confirm 과 합치기 가능?
storage 라는 리스트 안에 각각 행, 열, 블록 정보 저장.

pos check - 가능성 확정되면 그 행, 열, 블록에 겹치는 가능성만 제거하는 함수


sync - matrix에서 바뀐게 있다면 sudoku로 옮겨주는 함수

error_check - 규칙을 어긴 칸이 있나 확인하는 함수

complete - 완료되었나 확인(리스트인 칸이 있나 확인)

empty check - 빈 칸이 있나 확인 // 반복문에서 확인해줘서 필요없음

# 삭제된 함수

row_check, col_check, block_check - 겹치는 수를 제거해주는 함수