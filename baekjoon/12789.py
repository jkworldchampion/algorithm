num = int(input())
students = list(map(int, input().split()))

def can_snak(students):
    stack = []
    now = 1
    for student in students:
        if student == now:
            now += 1
        else:
            stack.append(student)
        while stack and stack[-1] == now:
            stack.pop()
            now += 1
    return not stack

print('Nice' if can_snak(students) else 'Sad')
