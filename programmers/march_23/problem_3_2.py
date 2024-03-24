#입력과 출력을 자유롭게 작성해주세요
alpha_rock = 0

def f(low, col):
    global alpha_rock
    mid_n = low//2
    mid_m = col//2
    if low%2==0 or col%2==0:
        return 0
        
    return 1 + 4 * f(mid_n, mid_m)

low, col = map(int, input().split())
print(f(low, col))
