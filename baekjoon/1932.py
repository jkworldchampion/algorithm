# 제출용

import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(n-2,-1,-1):
    for j in range(i+1):
        data[i][j] += max(data[i+1][j], data[i+1][j+1])

print(data[0][0])
