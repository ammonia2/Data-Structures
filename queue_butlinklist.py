#queue with linked list

head, tail, freeptr = -1, -1, None

class Node:
    def __init__(self):
        self.data = None
        self.next = None

def declare_q(q: list):
    global freeptr
    freeptr = 0
    for i in range(5):
        q.append(Node())
        q[i].next = i+1
    q.append(Node())
    q[5].next = -1

def enqueue(q :list, data:int):  
    global head, tail, freeptr
    if freeptr == -1:
        return print("The queue is full")
    curr = freeptr
    freeptr = q[curr].next
    
    q[curr].data = data
    if head == -1: 
        tail = curr
        head = curr
        q[curr].next = None
        return
    prev, q[curr].next = tail, None
    tail = curr
    q[prev].next = curr

def dequeue(q:list):
    global head, tail, freeptr
    if head == -1:
        return print("The queue is already empty")
    if tail == head:
        tail -= 1
        temp = freeptr
        freeptr, q[head].data = head, None
        head -= 1
        q[freeptr].next = temp
        return
    
    temp = head
    head = q[temp].next
    q[temp].data, q[temp].next = None, freeptr
    freeptr = temp

def print_q(q: list):
    global head, tail
    if head == -1:
        return print("The linked queue is empty")
    curr = head
    outstr = ""
    while curr != None:
        outstr += str(q[curr].data) + '-->' if curr != tail else str(q[curr].data)
        curr = q[curr].next
    print(outstr)

queue = []
declare_q(queue)
enqueue(queue, 5.5)
enqueue(queue, 5.9)
enqueue(queue, 6.8)
enqueue(queue, 7.8)
enqueue(queue, 10.1)
enqueue(queue, 10.7)
dequeue(queue)

print_q(queue)