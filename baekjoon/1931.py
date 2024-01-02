import sys

num = int(sys.stdin.readline())
meeting = []

for _ in range(num):
    meeting_start, meeting_end = map(int, sys.stdin.readline().split())
    meeting.append((meeting_start, meeting_end))

meeting.sort(key=lambda x:(x[1], x[0]))  # 처음엔 끝나는게 빠른순으로, 같으면 시작이 빠른 순으로
count = 1
now = meeting[0]

for i in range(1,num):  # 아 쉬바 처음꺼 빼줘야함
    if meeting[i][0] >= now[1]:
        count += 1
        now = meeting[i]

print(count)
