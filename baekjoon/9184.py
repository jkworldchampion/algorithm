# 제출 ver
import sys

def dynamic_ff(a,b,c):
    # dynamic 정보를 담을 list
    dynamic_map = [[[1048576 for _ in range(51)] for _ in range(51)] for _ in range(51)]  # 초기값에 주의하자
    
    for i in range(51):
        for j in range(51):
            for k in range(51):
                if (i<=0) or (j<=0) or (k<=0):
                    dynamic_map[i][j][k] = 1
                elif (i>20) or (j>20) or (k>20):
                    dynamic_map[i][j][k] = dynamic_map[20][20][20]
                elif (i<j) and (j<k):
                    dynamic_map[i][j][k] = dynamic_map[i][j][k-1] + dynamic_map[i][j-1][k-1] - dynamic_map[i][j-1][k]
                else:
                    dynamic_map[i][j][k] = dynamic_map[i-1][j][k] + dynamic_map[i-1][j-1][k] + dynamic_map[i-1][j][k-1] - dynamic_map[i-1][j-1][k-1]

    return dynamic_map[a][b][c]


while(True):
    a, b, c = map(int, input().split())
    if (a==-1) & (b==-1) & (c==-1):
        break
    elif (a<=0) or (b<=0) or (c<=0):
        print(f'w({a}, {b}, {c}) = ', end='')
        print(1)
    else:
        print(f'w({a}, {b}, {c}) = ', end='')
        print(dynamic_ff(a, b, c))
