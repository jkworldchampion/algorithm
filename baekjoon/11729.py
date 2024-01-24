n = int(input())

def hanoi_num(n):
    if n == 1:
        return 1
    else:
        return 2*hanoi_num(n-1) + 1


def hanoi_move(n, a, b, c):  # 이렇게 신기한 방법도 있구나..
    if n == 1:
        print(a, c)
    else:
        hanoi_move(n-1, a, c, b)
        print(a, c)
        hanoi_move(n-1, b, a, c)
        


print(hanoi_num(n))
hanoi_move(n, 1, 2, 3)
