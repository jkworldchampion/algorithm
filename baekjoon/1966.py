import sys

def when_print(data, where):
    now = -1
    order_num = 1
    while (True):
        now+=1
        if now>=len(data):
            now=0

        if data[now] == max(data):
            if where==now:
                return order_num
            data.pop(now), now, where
            now-=1
            if now<where:
                where-=1
            order_num+=1

case_num = int(sys.stdin.readline())
for _ in range(case_num):
    length, where = map(int, sys.stdin.readline().split())   
    input_data = list(map(int, sys.stdin.readline().split()))

    print(when_print(input_data, where))
