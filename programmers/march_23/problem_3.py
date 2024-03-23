def what_is_it(gen, index):
        if gen == 1:
            return "Rr"
        
        parent = what_is_it(gen-1, (index-1)//4+1)
        if parent=="RR" or parent=="rr":
            return parent

        if index%4 == 0:
            return "rr"
        elif index%4 == 1:
            return "RR"
        else:
            return "Rr"

def solution(queries):
            
    answer = []
    for i in queries:
        answer.append(str(what_is_it(int(i[0]), int(i[1]))))
    return answer
