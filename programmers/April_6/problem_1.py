def solution(keymap, targets):
    answer = []
    ar = {}
    
    # 최소값의 key map을 만듦
    for key in keymap:
        for i in range(len(key)):
            if key[i] in ar:
                ar[key[i]] = min(i+1, ar[key[i]])
            else:
                ar[key[i]] = i+1
    
    for target in targets:
        cnt = 0
        for ch in target:
            if ch in ar:
                cnt += ar[ch]
            else:
                cnt = -1
                break
        answer.append(cnt)
    
    
#     # 각 질문에 대한 탐색
#     for target in targets:
#         total = 0
        
#         for ch in target: 
            
#             # 전체 조건 체크 변수
#             ck = False
            
#             cnt = 999  # 최대 100글자 이상의 위치값
            
#             for key in keymap:
                
#                 if ch in key:
                    
#                     cnt = min(key.index(ch)+1, cnt)
#                     ck = True
                    
#             if not ck:
#                 total = -1
#                 break
#             else:
#                 total += cnt
#         answer.append(total)
    
    return answer
