### 전체 합치기 ###

# 필요한 함수 정의
def dfs(x, y):
    global field
    x_move = [0,1,0,-1]
    y_move = [1,0,-1,0]
    
    field[y][x] = 0

    for i in range(4):
        if ((m>x+x_move[i]))and((x+x_move[i])>=0)and((n>y+y_move[i]))and((y+y_move[i])>=0):
            if field[y+y_move[i]][x+x_move[i]]==1:
                dfs(x+x_move[i], y+y_move[i])

# 입력부
t = int(input())

## t번만큼 시행해야한다
for _ in range(t):

    m, n, k = map(int, input().split())
    field = [[0]*m for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    # 연산시행
    for i in range(n):
        for j in range(m):
            if field[i][j]==1:
                count+=1
                dfs(j,i)

    print(count)
