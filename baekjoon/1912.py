# 10만개의 데이터, 1초 = n logn
n = int(input())
data = list(map(int, input().split()))

for i in range(1, n):
    data[i] = max(data[i], data[i-1]+data[i])   # 핵심 생각
print(max(data))
