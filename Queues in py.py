class Queue:
    def __init__(self, limit):
        self.q = [0, 1, 2]
        self.pointer = len(self.q) - 1 #points to last element *modify if list input
        self.limit = limit

    def enque(self, data):
        if self.pointer < self.limit - 1: 
            self.q.insert(self.pointer + 1, data) #adds to next free space
            self.pointer += 1
        else:
            print('Queue overflow')
            self.q.pop(0)
            self.q.insert(self.pointer, data)
        print(self.q)

    def deque(self):
        if len(self.q)>0:
            self.q.pop(0)
            self.pointer -= 1
            print(self.q)
        else:
            print('Queue is empty')

    def reverse(self, newq):
        while len(self.q) > 0:
            temp = q1.pop()
            newq.push(temp)
        print(newq)    
        

q1 = Queue(6)


q2 = Queue(6)
q1.reverse(q2)

