n, m = map(int, input().split())
global data_list
data_list = []

def find_n(now, m):  # 인수 하나를 더 쓰자
  if m == 1:
    for i in range(now, n+1):  # now를 추가해서 지금이후만 돌림
      data_list.append(i)
      print(*data_list)
      del data_list[len(data_list)-1]
  else:
    for i in range(now, n+1):  # 마찬가지
      data_list.append(i)
      find_n(i,m-1)
      del data_list[len(data_list)-1]

find_n(1,m)
