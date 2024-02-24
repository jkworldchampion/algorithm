n = int(input())
data = [0]*10001
for _ in range(n):
    data[int(input())] += 1
for index, data in enumerate(data):
    if data!=0:
        for _ in range(data):
            print(index)
