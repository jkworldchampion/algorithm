n = int(input())
data = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    data[i] = list(map(int, input()))

def is_group(m, i, j, data):
    now = data[i][j]
    result = 1
    for k in range(i, i+m):
        for l in range(j, j+m):
            if data[k][l] != now:
                result = 0
                break
    if result:
        print(now, end='')
    else :
        m = m//2
        print("(", end='')
        is_group(m, i, j, data)
        is_group(m, i, j+m, data)
        is_group(m, i+m, j, data)
        is_group(m, i+m, j+m, data)
        print(")", end='')


is_group(n, 0, 0, data)
