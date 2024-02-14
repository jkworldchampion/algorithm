import sys
# 제출용

n = int(sys.stdin.readline())

if n==0:
    print(0)
    exit()

def rround(n):
    if n-int(n)>=0.5:
        return int(n)+1
    else:
        return int(n)

data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

slice_num = rround(n*0.15)
data.sort()
# 여기가 문제였음
if slice_num!=0:
    data = data[slice_num:-slice_num]

slice_mean = rround(sum(data)/len(data))

print(slice_mean)
