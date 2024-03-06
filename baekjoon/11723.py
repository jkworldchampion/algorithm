import sys

n = int(input())
S = [0] * 21

for _ in range(n):
    # colab에서는 sys.stdin.readline이 작동하지 않음.
    # order = list(map(str, sys.stdin.readline().rstrip().split()))
    order = list(map(str, input().split()))
    if order[0]=="add":
        S[int(order[1])] = 1

    elif order[0]=="remove":
        S[int(order[1])] = 0

    elif order[0]=="check":
        if S[int(order[1])]==1:
            print(1)
        else:
            print(0)

    elif order[0]=="toggle":
        S[int(order[1])] = 0 if S[int(order[1])] else 1

    elif order[0]=="all":
        S = [1] * 21

    elif order[0]=="empty":
        S = [0] * 21

# memory 사용량 pypy > python
# 시간 python > pypy
