# 브루트포스
to_go = int(input())
broken_button_num = int(input())
if broken_button_num != 0:
    broken_button = list(map(int, input().split()))
else:
    broken_button = []

min_can_go = abs(100-to_go)

for i in range(1000000):
    i = str(i)

    for j in i:
        if int(j) in broken_button:
            break
    else: # 이런 신기한 if else문도 가능하다.
        min_can_go = min(min_can_go, abs(int(i)-to_go)+len(str(i)))
print(min_can_go)
