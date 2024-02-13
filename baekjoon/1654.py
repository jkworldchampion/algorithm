# 이진탐색을 이용하자
k, n = map(int, input().split())
# lan = [int(input()) for _ in range(K)]
# 이런 문법도 사용을 한다..
lines = []
for _ in range(k):
    lines.append(int(input()))

start, end = 1, max(lines)

while start <= end:
    mid = (start+end)//2
    line_num = 0 # 랜선의 개수
    for i in lines:
        line_num += i//mid
    if line_num >= n:
        start = mid+1
    else:
        end = mid-1
print(end)
