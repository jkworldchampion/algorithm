import heapq
import sys

q = []

num = int(sys.stdin.readline())
for _ in range(num):
    order = int(sys.stdin.readline())
    if order :
        heapq.heappush(q, order)
    else:
        if len(q):
            print(heapq.heappop(q))
        else:
            print("0")
