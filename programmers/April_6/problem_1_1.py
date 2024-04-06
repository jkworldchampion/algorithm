def solution(participant, completion):
    com_dic = {}
    for i in completion:
        if i in com_dic:
            com_dic[i] += 1
        else:
            com_dic[i] = 1
    
    for j in participant:
        if j in com_dic:
            com_dic[j] -= 1
        else:
            return j
    
    answer = [k for k, v in com_dic.items() if v == -1][0]
    
    # 효율성 실패
    # for i in participant:
    #     if i in completion:
    #         completion.remove(i)
    #     else:
    #         answer = i
    #         break
    return answer
