from collections import deque
import sys

deque = deque()

n = int(sys.stdin.readline())
for _ in range(n):
    order = list(map(str, sys.stdin.readline().split()))
    if order[0]=="push_front":
        deque.appendleft(order[1])
    elif order[0]=="push_back":
        deque.append(order[1])
    elif order[0]=="pop_front":
        if len(deque):
            print(deque.popleft())
        else:
            print(-1)
    elif order[0]=="pop_back":
        if len(deque):
            print(deque.pop())
        else:
            print(-1)
    elif order[0]=="size":
        print(len(deque))
    elif order[0]=="empty":
        if len(deque):
            print(0)
        else:
            print(1)
    elif order[0]=="front":
        if len(deque):
            print(deque[0])
        else:
            print(-1)
    elif order[0]=="back":
        if len(deque):
            print(deque[len(deque)-1])
        else:
            print(-1)
    else:
        exit()
