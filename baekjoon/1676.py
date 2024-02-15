n = int(input())
result = 1
for i in range(1,n+1):
    result *= i
result = str(result)
start = len(result)-1
count = 0
now = result[start]
while now=='0':
    count+=1
    start-=1
    now=result[start]

print(count)
