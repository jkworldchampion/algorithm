a, b = map(int, input().split())
max_divide = 0
min_multiply = 0
for i in range(1,min(a,b)+1):
    if (a%i==0)&(b%i==0):
        max_divide = i
min_multiply = (a*b)//max_divide
print(max_divide)
print(min_multiply)
