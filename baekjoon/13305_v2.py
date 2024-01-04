n = int(input())
L = list(map(int,input().split()))
costs = list(map(int,input().split()))

res = L[0] * costs[0]   # 연료 * 가격
m = costs[0]            # 최소 비용 초기화
dis = 0                 # 거리 초기화
for i in range(1, n-1):
  if costs[i] < m:      # 현재 연료 가격이 최소 비용보다 작은지 확인
    res += m*dis        # 이전 구간 비용을 총합에 추가
    dis = L[i]          # 새로운 구간을 위해 거리 초기화
    m = costs[i]        # 최소 비용 업데이트
  else:                 # 현재 가격이 최소가 아니라면 거리를 누적
    dis += L[i]

  if i == n-2:          # n-1까지 반복이니깐 마지막 정거장인지 확인하고 총 비용 업데이트
    res += m*dis

print(res)
