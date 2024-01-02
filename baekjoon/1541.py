data = input().split('-')
total_data = []

for i in data:
    data_sum = 0
    plus_data = i.split('+')
    for j in plus_data:
        data_sum += int(j)
    total_data.append(data_sum)

total = total_data[0]

for i in range(1, len(total_data)):
    total -= total_data[i]
print(total)
