answer = 0

def brute_force_dfs(event, total, ability, choice):
    global answer
    rows = len(ability)
    cols = len(ability[0])
    if event == cols:
        answer = max(answer, total)
    else:
        for i in range(rows):
            if choice[i]==0:
                choice[i] = 1
                brute_force_dfs(event+1, total+ability[i][event], ability, choice)
                choice[i] = 0



def solution(ability):
    global answer
    answer = 0
    choice = [0]*len(ability)
    brute_force_dfs(0,0,ability, choice)

    return answer
