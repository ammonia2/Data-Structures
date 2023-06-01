"""this tree isn't balanced. always leans leftwards. """
class Node:
    def __init__(self, item):
        self.data = item
        self.right = None
        self.left = None

def create_tree(root: Node, array: list): #all g except the balance case.
    if len(array) < 2:
        return print("Invalid array")
    root.left = Node(array[1])
    root.right, lev = Node(array[2]), 1
    for i in range(3, len(array), 2):
        curr = root
        if lev % 2 != 0:
            while curr.left != None:
                curr = curr.left
        else:
            while curr.right!= None:
                curr = curr.right
        curr.left = Node(array[i])
        if i+1 < len(array):
            curr.right  = Node(array[i+1])
        lev +=1

def count_levels(root:Node, lev=1): # good
    curr = root
    if curr == None:
        lev = 0
    elif curr.left:
        lev+=1
        lev = count_levels((root.left), lev)
    #global rooot
    #if curr == rooot:
        #print(lev)
    return lev

def graphical_print(root: Node, levels):
    start, ispace = levels-1, 0
    while start >= 0:
        ispace += 2**start
        start-=1
    #print(ispace)
    print(' '*(ispace), end='')
    print(root.data)
    level = levels
    while level >= 0:
        # print(' '*(ispace - 2**(i+1)), end='')
        # print(root.left.data)
        # root = root.left
        spacing_func(root, level, ispace)
        level -= 1

def spacing_func(curr: Node, level, ispace):
    p_list = [" "]*(ispace*2)
    if curr.left:
        new_id = ispace-(2**(level+1))-1
        #print(new_id)
        p_list[new_id] = str(curr.left.data)
    #if curr.right:
        #p_list[ispace+(2**(level+1))-1] = str(curr.right.data)
    #print(p_list)
    p_str = ""
    for x in range(len(p_list)):
        p_str += p_list[x]
    print(p_str)

array = [1, 12, 9, 5, 6, 10]
rooot = Node(array[0])
create_tree(rooot, array)
levels = count_levels(rooot)
graphical_print(rooot, levels)