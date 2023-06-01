head_ptr = -1
free_ptr = 0

class node:
    def __init__(self):
        self.data = "ee"
        self.pointer = 0

def initialise(link_l): #working
    global head_ptr, free_ptr
    head_ptr, free_ptr = -1, 0
    for i in range(5):
        link_l.append(node())
        link_l[i].pointer = i + 1
    link_l.append(node())
    link_l[5].pointer = -1

def insert(link_l, input): # insert at the next free node
    global head_ptr, free_ptr
    
    if free_ptr==-1: return print("List fullllllll")
    
    curr_ptr = head_ptr
    next_ptr = free_ptr

    if head_ptr == -1:
        head_ptr = next_ptr
    
    else: #potato.
        while link_l[curr_ptr].pointer != -1:
            curr_ptr = link_l[curr_ptr].pointer
        link_l[curr_ptr].pointer = next_ptr

    link_l[next_ptr].data = input
    free_ptr = link_l[next_ptr].pointer
    link_l[next_ptr].pointer = -1

def remove(link_l, delete):
    global free_ptr, head_ptr
    if head_ptr == -1:
        return print("The list is empty")
    
    curr_ptr = head_ptr

    while link_l[curr_ptr].data != delete:
        prev = curr_ptr
        curr_ptr = link_l[curr_ptr].pointer
    
    if curr_ptr == head_ptr:
        head_ptr = link_l[curr_ptr].pointer
    else:
        link_l[prev].pointer = link_l[curr_ptr].pointer

    link_l[curr_ptr].pointer = free_ptr
    free_ptr = curr_ptr

def printlist(link_l): #good
    global head_ptr, free_ptr
    if head_ptr == -1:
        return print("Linked list is empty")
    
    llstr = ""
    curr_ptr = head_ptr
    while curr_ptr != -1:
        llstr += link_l[curr_ptr].data+"--> " if link_l[curr_ptr].pointer!=-1 else link_l[curr_ptr].data
        curr_ptr = link_l[curr_ptr].pointer
    return print(llstr)

def search(link_l, element):
    found = False
    curr_ptr = head_ptr
    while curr_ptr != -1:
        if link_l[curr_ptr].data == element:
            print("Found", element, "at position", curr_ptr)
            found = True
        curr_ptr = link_l[curr_ptr].pointer
    if not found:
        print("Couldn't find", element)

l_list = []
initialise(l_list)
# print(l_list[0].data)
# print(l_list[1].data)
insert(l_list, "one")
insert(l_list, "two")
insert(l_list, "three")
insert(l_list, "four")
insert(l_list, "five")
insert(l_list, "six")
insert(l_list, "seven")
search(l_list, "four")
remove(l_list, "three")
printlist(l_list)