import sys
n = int(input())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
data.sort()
for _ in data:
    print(_)
