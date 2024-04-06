def solution(a):
    answer = 0
    alive = [0] * (len(a))

    min_value = a[0]
    for i in range(1,len(a)):
        if a[i] < min_value:
            alive[i] += 1
        min_value = min(min_value, a[i])
    
    min_value = a[-1]
    for i in range(len(a)-1,-1, -1):
        if a[i] < min_value:
            alive[i] += 1
        min_value = min(min_value, a[i])
        
    for i in range(1,len(a)-1):
        if alive[i] != 0:
            answer += 1
    
    # 시간초과
#     alive = [0] * (len(a))
#     for i in range(1,len(a)-1):
#         front_min = min(a[:i])
#         back_min = min(a[i+1:])
        
#         if (front_min > a[i]) or (back_min > a[i]):
#             alive[i] = 1
        
#     answer = sum(alive) + 2
    return answer + 2
