n = int(input())
for i in range(1, n):
    num_list = list(map(int, str(i)))
    if (i+sum(num_list))==n:
        print(i)
        exit()
print(0)
