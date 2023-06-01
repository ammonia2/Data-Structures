#stack with linked list
freeptr = None
Top = None

class Node:
    def __init__(self):
        self.data = None
        self.next = None

def declare_stack(stackarray:list):
    global freeptr, Top
    freeptr = 0
    stackarray.insert(0, Node())
    stackarray[0].next = -1
    for i in range(1, 5):
        stackarray.insert(0, Node())
        stackarray[0].next =5-i
    #Top = len(stackarray)-1

def insert(stackarray, data):
    global Top, freeptr
    if freeptr == None:
        return print(" Stack is full")
    
    new_ptr = freeptr
    
    stackarray[new_ptr].data = data
    freeptr =stackarray[freeptr].next
    stackarray[new_ptr].next = Top
    Top = new_ptr
    
    #if Top != None: Top -=1

def remove(stackarray):
    global Top, freeptr
    if Top == None:
        return print("The stack is empty")
    temp = freeptr
    freeptr = Top
    stackarray[Top].data = None
    Top = stackarray[freeptr].next
    
    stackarray[freeptr].next = temp
    del temp
    

def print_stack(stackarray):
    global Top, freeptr
    count = Top
    if stackarray[count].data == None:
        return print("The stack linked list is empty")
    outstr = ""
    while count !=-1:
        outstr += str(stackarray[count].data) + '-->' if count !=0 else str(stackarray[count].data)
        count -=1
    print(outstr)

ll_stack = [Node] * 5
declare_stack(ll_stack)
insert(ll_stack, "fiend")
insert(ll_stack, "fiend")
insert(ll_stack, "fiend")
insert(ll_stack, "fiend")
remove(ll_stack)
#insert(ll_stack, "fiend")
print_stack(ll_stack)