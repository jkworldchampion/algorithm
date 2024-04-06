def bfs(cut, n, graph):
    # 방문값
    visit = [0 for i in range(n+1)]
    # 양쪽 위치에 방문값 처리
    visit[cut[0]] = 1  # 중요한 부분
    visit[cut[1]] = 1
    
    # bfs의 시작값 세팅
    q = [cut[0]]
    
    cnt = 1
    
    while q:
        x = q.pop(0)
        # x에 연결된 모든 그래프에 대해서 bfs
        for i in graph[x]:
            if visit[i] == 0:
                q.append(i)
                cnt += 1
                visit[i] = cnt
    print("visit: ", visit)
    return cnt
                

def solution(n, wires):
    answer = n
    
    # data를 그래프 구조화 [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    graph = [[]for _ in range(n+1)]
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)
    
    # 모든 위치에서 bfs 실행
    for i in wires:
        # bfs의 최종 return은 연결된 개수
        cnt = bfs(i, n, graph)
        print(i)
        print(cnt)
        
        # 양쪽의 개수 차이(가장 작은 값)
        answer = min(answer, abs(cnt - (n - cnt)))
    
    return answer
