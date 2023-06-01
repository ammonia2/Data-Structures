"binary tree using linked list(using lists)"
freeptr = None
root = None

class node:
    def __init__(self) -> None:
        self.data=None
        self.right = None
        self.left = None

def initialise(ll: list, size):
    global root, freeptr
    ll = [0] * size
    for i in range(0, size-1): 
        ll[i] = node()
        ll[i].right = i+1
        i+=1
    ll[size-1] = node()
    freeptr = 0
    return ll


def insert(ll: list, data: str) ->None:
    global root, freeptr
    if freeptr == None:
        return print("The tree is full")
    #root case
    if root == None:
        root = freeptr
        freeptr = ll[freeptr].right
        ll[root].data = data
        ll[root].right = None
        return 
    #normal case
    curr = root
    while curr != None:
        prev = curr
        curr =  ll[prev].right if data > ll[prev].data else ll[prev].left
    new_node= freeptr
    freeptr = ll[freeptr].right
    if data > ll[prev].data: ll[prev].right = new_node
    else: ll[prev].left = new_node
    ll[new_node].data = data
    ll[new_node].right = None
    

def in_ordertraversal(ll: list, curr): # loop : (visit left --> print root --> visit right)
    global root
    if ll[curr].left:
        in_ordertraversal(ll, ll[curr].left)
    print(ll[curr].data , '-->', end=' ')
    if ll[curr].right:
        in_ordertraversal(ll, ll[curr].right)

def pre_ordertraversal(ll: list, curr): # loop : (print root --> visit left --> visit right)
    global root
    print(ll[curr].data , '-->', end=' ')
    if ll[curr].left:
        in_ordertraversal(ll, ll[curr].left)
    if ll[curr].right:
        in_ordertraversal(ll, ll[curr].right)

def post_ordertraversal(ll:list, curr): # loop : (visit left --> visit right --> print root)
    global root
    if ll[curr].left:
        in_ordertraversal(ll, ll[curr].left)
    if ll[curr].right:
        in_ordertraversal(ll, ll[curr].right)
    print(ll[curr].data , '-->', end=' ')

linklist = -1
linklist = initialise(ll =linklist, size=8)
insert(linklist, 'M')
insert(linklist, 'B')
insert(linklist, 'P')
insert(linklist, 'A')
insert(linklist, 'X')
insert(linklist, 'C')
insert(linklist, 'O')

in_ordertraversal(linklist, root)
pre_ordertraversal(linklist, root)
post_ordertraversal(linklist, root)