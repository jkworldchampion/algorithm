import sys
n, k = map(int, sys.stdin.readline().split())
index = 0
index_sum = 0
line = list(range(1,n+1))
is_print = [1]*n
# 머리에서 이루어지는 그대로 간다
print("<", end='')
count = n
# n번 만큼만 출력하면 종료
while count:
    if index == n:
        index = 0

    index_sum += is_print[index]

    if index_sum == k:
        if count == 1:
            print(line[index], end='')
            print(">")
            count -= 1
        else:
            print(line[index], end=', ')
            count -= 1
            is_print[index] = 0
            index_sum = 0
    if index == n:
        index = 0
    
    index += 1
