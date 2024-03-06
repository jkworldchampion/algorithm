n, m = map(int, input().split())
sites = {}
for _ in range(n):
    site, password = map(str, input().split())
    sites[site] = password

for _ in range(m):
    print(sites.get(input()))


# 이 코드에서는 문자열을 받기때문에 sys.stdin.readline을 쓰기위해선 공백처리에 주의해야한다.
