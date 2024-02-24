n = int(input())

bee_home = [1]
for i in range(20000):
    bee_home.append(bee_home[i]+6*(i+1))
count = 1
for j in bee_home:
    if n <= j:
        print(count)
        break
    count+=1
