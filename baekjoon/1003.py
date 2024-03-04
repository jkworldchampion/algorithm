# 밑에서 구한 규칙을 갖고 답을 찾는다
def fibo_call(x):
    fibo_result = [1]*(x+2)
    for i in range(x):
        fibo_result[i+2] = fibo_result[i] + fibo_result[i+1]
    print(fibo_result[x-2], end=' ')
    print(fibo_result[x-1])

t = int(input())
for _ in range(t):
    n = int(input())
    if n==0:
        print(1, 0)
    elif n==1:
        print(0, 1)
    else:
        fibo_call(n)
