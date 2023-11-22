from sys import stdin

data, num = [], int(input())
cnt = 0

for _ in range(num):
    order = stdin.readline().split()
    if order[0] == "push":
        data.append(int(order[1]))
    elif order[0] == "pop":
        if len(data) == cnt:
            print(-1)
        else :
            print(data[cnt])
            cnt += 1
    elif order[0] == "size":
        print(len(data)-cnt)
    elif order[0] == "empty":
        if len(data) == cnt:
            print(1)
            data = []
            cnt = 0
        else:
            print(0)
    elif order[0] == "front":
        if len(data) > cnt: print(data[cnt])
        else: print(-1)
    else :
        if len(data) > cnt: print(data[len(data)-1])
        else: print(-1)
