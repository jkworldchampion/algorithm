n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(list(map(str, input())))


result = 64
for i in range(n-7):  # 체스판을 옮기기 위해
    for j in range(m-7):
        white = 0
        black = 0

        # 체스판에서 바꿔야하는 조각 개수
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2==0:
                    if board[k][l]=='W':
                        white += 1
                    else:
                        black += 1
                else:
                    if board[k][l]=='B':
                        white += 1
                    else:
                        black += 1
        result = min(result, min(white, black))
print(result)
