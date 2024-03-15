now = 100
button_can_go = []   # 갈 수 있는 번호

# 일단 100번 그대로이면 0을 출력하고, 끝내기
if to_go==100:
    print(0)
    # exit()

for i in str(to_go):
    # 해당 번호가 고장났다면
    i = int(i)
    if i in broken_button:
        # 가장 가까운 고장이 나지 않은 번호로 바꾼다
        while (i in broken_button):
            i += 1
            if i==10:   # 10개가 다 고장 -> 필요
                i=0 
        print(i)
        button_can_go.append(i)
    # 고장이 안났다면
    else: 
        print(i)
        button_can_go.append(i)

result = 0
for index, i in enumerate(button_can_go):
    result += i*(10**(len(button_can_go)-1-index))
print(result-to_go)
