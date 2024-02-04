# import sys
# input = sys.stdin.readline
class stack:
    data = list()

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data)==0:
            return -1
        else:
            return self.data.pop()

    def size(self):
        return len(self.data)

    def empty(self):
        if len(self.data) == 0:
            return 1
        else:
            return 0

    def top(self):
        if len(self.data)==0:
            return -1
        else:
            return self.data[len(self.data)-1]

stack = stack()
num = int(input())
for _ in range(num):
    command = list(map(str, input().split()))
    if len(command)==2:
        stack.push(int(command[1]))
    else:
        if command[0] == "top":
            print(stack.top())
        elif command[0] == "size":
            print(stack.size())
        elif command[0] == "empty":
            print(stack.empty())
        else:
            print(stack.pop())
