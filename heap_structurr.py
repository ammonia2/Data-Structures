#Heap data structure.
"Min-Heap is when childs are greater than roots. Max-Heap is when childs are smaller than roots."

class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def c_tree(root:node, array:list): #creates a complete b_tree
    if len(array) < 2:
        return print("Invalid array")
    root.left = node(array[1])
    root.right, lev = node(array[2]), 1
    for i in range(3, len(array), 2):
        curr = root
        if lev % 2 != 0:
            while curr.left != None:
                curr = curr.left
        else:
            while curr.right!= None:
                curr = curr.right
        curr.left = node(array[i])
        if i+1 < len(array):
            curr.right  = node(array[i+1])
        lev +=1

def max_heapify(curr:node, max):
    
    if curr.right and curr.right.data > max.data:
        max = curr.right
    if curr.left and curr.left.data > max.data:
        max = curr.left
    if max != curr:    
        temp = curr.data
        curr.data = max.data
        max.data = temp
    
    if curr.left: max_heapify(curr.left, curr.left)
    if curr.right: max_heapify(curr.right, curr.right)
    return

def inorderTraversal(curr):  #visit left --> print root --> visit right
        if curr.left:
            inorderTraversal(curr.left)
        print(curr.data)
        if curr.right:
            inorderTraversal(curr.right)

array = [1, 12, 9, 5, 6, 10]
rooot = node(array[0])
c_tree(rooot, array)
inorderTraversal(rooot)
max_heapify(rooot, rooot)
print("-----------------------------------")
inorderTraversal(rooot)