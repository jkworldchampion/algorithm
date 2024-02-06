t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    room = (n%h)*100 + (n//h)+1

    if n%h==0:
        room = h*100 + (n//h)
        if h==1:
            room = 100 + n
    print(room)
