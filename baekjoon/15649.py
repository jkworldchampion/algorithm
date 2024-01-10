n, m = map(int, input().split())

s = list()
def bfs():
    if len(s) == m:
        print(' '.join(map(str, s)))   # 여기서 map 사용 주의

    for i in range(1, n+1):
        if i not in s:
            if len(s) == 0:
                s.append(i)
                bfs()
                s.pop()
            else:
                s.append(i)
                bfs()
                s.pop()
bfs()
