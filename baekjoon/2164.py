# 2^n으로 나누기
n = int(input())
if n==1:
    print(1)
    exit()
elif n==2:
    print(2)
    exit()
for i in range(n):
    if 2**i > n:
        big_n = i-1
        break
if n==(2**big_n):
    print(n)
else:
    print((n-(2**big_n))*2)
