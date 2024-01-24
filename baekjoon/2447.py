# 다른 풀이
def star(n):
    if n == 1:
        return ['*']

    stars = star(n//3)
    l = []

    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s + ' '*(n//3) + s)
    for s in stars:
        l.append(s*3)
    return l

n = int(input())
print('\n'.join(star(n)))
