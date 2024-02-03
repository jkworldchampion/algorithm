n = int(input())
data = []
for _ in range(n):
    now = str(input())
    if any(now in l for l in data):
        continue
    else:
        data.append((now, len(now)))
data.sort(key=lambda x:(x[1], x[0]))
for i in range(len(data)):
    print(data[i][0])
