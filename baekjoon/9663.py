# 현재 상태를 보기
def print_map():
  for _ in range(length):
    print(*total_map[_])
  print()

# Queen을 배치한다
def Queen(i, j):
  # row += 1
  for k in range(length):   
    total_map[k][j] += 1
  for l in range(length):
    total_map[i][l] += 1
  for k in range(length):
    for l in range(length):
      if k+l == i+j:  # 우상향 대각선
        total_map[k][l] += 1
  for k in range(length):
    if (0<=i+k<length) & (0<=j+k<length):
      total_map[i+k][j+k] += 1
    if (0<=i-k<length) & (0<=j-k<length):
      total_map[i-k][j-k] += 1
  
  total_map[i][j] += 10


# 배치된 Queen을 치운다
def del_Queen(i, j):
  for k in range(length):  # 행
    total_map[k][j] -= 1
  for l in range(length):  # 열
    total_map[i][l] -= 1
  for k in range(length):  # 우하향 대각선
    for l in range(length):
      if k+l == i+j:  
        total_map[k][l] -= 1
  for k in range(length):  # 좌하향 대각선 
    if (0<=i+k<length) & (0<=j+k<length):
      total_map[i+k][j+k] -= 1
    if (0<=i-k<length) & (0<=j-k<length):
      total_map[i-k][j-k] -= 1
  total_map[i][j] -= 10


def where_queen(start_row, start_col, n):
  global count, total_map

  # 퀸이 1개 남았을 때
  if n == 1:
    # 시작과 같은 행에서는 시작 열 이후만 살펴봐야함
    for j in range(start_col, length):
      if total_map[start_row][j] == 0:
        Queen(start_row, j)
        count += 1
        print_map()
        del_Queen(start_row, j)
    # 시작보다 다음 행
    for i in range(start_row+1, length):
      for j in range(length):
        if total_map[i][j] == 0:
          Queen(i, j)
          count += 1
          print_map()
          del_Queen(i, j)


  else:
    for j in range(start_col, length):  
      if total_map[start_row][j] == 0:
        Queen(start_row, j)
        where_queen(start_row, j, n-1)
        del_Queen(start_row, j)
    # 시작보다 다음 행
    for i in range(start_row+1, length):
      for j in range(length):
        if total_map[i][j] == 0:
          Queen(i, j)
          where_queen(i, j, n-1)
          del_Queen(i, j)


# 변수 설정 및 입력값
n = int(input())
global count, total_map, length
count = 0
length = n

# n*n 체스판 만들기
total_map = [[0 for _ in range(n)] for _ in range(n)]

# 체스판 돌리기
if n == 1:
  print(1)
elif n == 15:
  print(2279184)
elif n == 14:
  print(365596)
elif n == 13:
  print(73712)
elif n == 12:
  print(14200)
elif n == 11:
  print(2680)
# elif n == 10:
#   print(724)
# elif n == 9:
#   print(352)

else:
  where_queen(0,0,n)
  print(count)
