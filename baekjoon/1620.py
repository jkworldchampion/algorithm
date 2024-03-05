n, order = map(int, input().split())
dic = {}
for i in range(n):
    monster = input()
    dic[i+1] = monster
    dic[monster] = i+1

for _ in range(order):
    now_order = input()
    if now_order.isdigit():
        print(dic.get(int(now_order)))
    else:
        print(dic.get(now_order))
