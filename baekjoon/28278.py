import sys

class Stack:

    data = []
    num = 0

    def add(self, x):
        self.data.append(x)
        self.num += 1

    def out(self):
        if self.data:
            print(self.data.pop())
            self.num -= 1
        else:
            print(-1)

    def sizeof(self):
        print(self.num)

    def isempty(self):
        if self.num==0:
            print(1)
        else : 
            print(0)
    
    def out5(self):
        if self.data:
            print(self.data[len(self.data)-1])
        else:
            print(-1)


num_range = int(sys.stdin.readline().rstrip())

stack = Stack()

for _ in range(num_range):
    input_order = list(map(int, sys.stdin.readline().rstrip().split()))
    if input_order[0] == 1:
        stack.add(input_order[1])
    elif input_order[0] == 2:
        stack.out()
    elif input_order[0] == 3:
        stack.sizeof()
    elif input_order[0] == 4:
        stack.isempty()
    else :
        stack.out5()
