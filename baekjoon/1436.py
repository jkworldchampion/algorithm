target = int(input())
count = 0
num = 665

while(True):
    if '666' in str(num):
        count += 1

    if count==target:
        break

    num+=1

print(num)
