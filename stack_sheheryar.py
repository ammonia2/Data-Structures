class Stack:
    def __init__(self, size):
        self.stack = ['']*size
        self.top = -1
        self.size = size

    def push(self, data):
        if self.top == 0: print("Stack is full.")
        if self.top == -1:
            self.top = self.size-1
            
        else:
            self.top = self.top-1
        print(self.top)
        self.stack[self.top] = str(data)

    def pop(self):
        if self.top == -1: print("The stack is empty.")
        if self.top == self.size-1:
            temp = self.stack[self.top]
            print("Element removed: ", temp)
            self.top = -1
        else:
            temp = self.stack[self.top]
            self.top = self.top+1

    def Printall(self):
        outstr = ''
        index = self.top
        print(self.top)
        if index == -1:
            print("The stack is empty")
        else:
            while index < self.size:
                outstr = outstr + str(self.stack[index]) + '-->'
                index = index +1
        print(outstr)

s = Stack(4)
s.push('A')
s.push('B')
#s.pop()
s.push('C')
s.pop()
s.Printall()