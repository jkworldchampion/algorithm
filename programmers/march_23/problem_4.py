import heapq

def solution(program):
    
    # 0번째가 프로그램 종료시간, 각 우선순위번호별 대기시간
    answer = [0] * 11
    
    # 우선순위 순으로 정렬
    program.sort(key=lambda x: (x[1], x[0]))
    
    time = 0
    
    # 중간 대기
    q = []
    
    # 남은, 대기 프로그램이 있는지
    while program or q:
        # 프로그램이 있고, 실행할 프로그램의 시작시간이 현 시간보다 앞에 있다면
        while program and program[0][1] <= time:
            # 모두다 대기에 걸기
            heapq.heappush(q, program.pop(0))
            # 정렬은 자동으로 [0]번째 우선순위 순으로 자동정렬
            
        # 프로그램은 있는데 대기중 프로그램이 없다면
        if program and not q:
            # 프로그램을 꺼내서 대기에 걸기
            heapq.heappush(q, program.pop(0))
            
            # 대기에 걸고 바로 꺼내서 실행 하기 위해 현시간을 세팅
            time = q[0][1]
        proinfo = heapq.heappop(q)
        # 현 프로그램의 대기시간
        answer[proinfo[0]] += time - proinfo[1]
        # 현 시간은 꺼낸 프로그램의 동작시간을 더함 // 프로그램 종료
        time += proinfo[2]
        
    answer[0] = time
    
        
        
    return answer
