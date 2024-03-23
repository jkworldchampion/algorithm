a, b = map(int, input().split())
list_a = {}
list_b = []
for _ in range(a):
    list_a[input()] = 1

for _ in range(b):
    list_b.append(str(input()))

result = []
for i in list_b:
    if i in list_a:
        result.append(i)

result.sort()
print(len(result))
for i in result:
    print(i)
