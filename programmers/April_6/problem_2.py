from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    cnt = len(enemy)

    # 시작시 무적권보다 게임 판수가 적으면 클리어
    if cnt <= k:
        return cnt
    
    q = []
    
    for i in range(cnt):
        # 매 라운드 마다 q에 넣어서 분석
        heappush(q, enemy[i])
        
        # q에 들어간 라운드가 k보다 크기 시작하면 분석
        if len(q) > k:
            # 가장 작은 수의 몬스터부터 내 병사를 사용
            mon = heappop(q)
            # 내 병사를 사용
            n -= mon
            
            # 내 병사가 0보다 작으면 전 라운드 끝
            if n <0:
                return i
    
    answer = cnt
    return answer
