def solution(input_string):
    # input_type = set(list(map(str, input_string)))
    input_type = []
    answer = []

    for i in range(len(input_string)):
        if input_string[i] in input_type:
            if input_string[i-1] != input_string[i]:
                if input_string[i] in answer:
                    continue
                else:
                    answer.append(input_string[i])
        else:
            input_type.append(input_string[i])
    
    answer.sort()
    answer = "".join(answer)
    if len(answer)==0:
        answer = "N"
    
    return answer
