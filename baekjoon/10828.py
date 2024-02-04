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
