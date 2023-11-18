n, m = map(int, input().split())
global data_list
data_list = []

def find_n(m):
  if m == 1:
    for i in range(1, n+1):
      data_list.append(i)
      print(*data_list)
      del data_list[len(data_list)-1]
  else:
    for i in range(1, n+1):
      data_list.append(i)
      find_n(m-1)
      del data_list[len(data_list)-1]

find_n(m)
