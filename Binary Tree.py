#recurion--recursion
class Node:
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def inorderTraversal(self):  #visit left --> print root --> visit right
        if self.left:
            self.left.inorderTraversal()
        print(self.data)
        if self.right:
            self.right.inorderTraversal()

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
                return        
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                return
    
    def search_node(self, val, branchnum = 0):
        if self.data == val:
            return print("Node is found at Branch no.:" , branchnum)
        elif self.data < val:
            if self.right:
                self.right.search_node(val, branchnum+1)
            else:
                return print("Node not found.")
        elif self.data > val:
            if self.left:
                self.left.search_node(val, branchnum+1)
            else:
                return print("Node not found.")

    def find_mid(self, mid, min, max):  #supplement to self.delete_node
        mid = self.data if self.data > min and self.data <= max else mid
        if self.right:
            mid = self.right.find_mid(mid, min, max)
        if self.right is None:
            return mid
        elif self.right is not None:
            return mid
        if self.left:
            mid = self.right.find_mid(mid, self.right.data)
        return mid
    
    def delete_node(self, val, prev = None):
        if self.data == val:
            if self.right is not None and self.left is not None:
                new = self.left.find_mid(self.left.data, self.left.data, self.right.data)
                self.data = new
                self.left.delete_node(new, self.right)
            elif self.left and self.right is None:
                self.data = self.left.data
                self.left = None
            elif self.right and self.left is None:
                self.data = self.right.data
                self.right = None
            else:
                if prev.left == val:
                    prev.left = None
                else:
                    prev.right == None
                self.data = None
        elif val < self.data:   # fix startup
            self.left.delete_node(val, self.left)
        elif val > self.data:
            self.right.delete_node(val, self.right)
        
    """def Btree(self, index = 1):   #flawwwwwweed insert
        node = Node(data=self.nlist[index])
        goright = True if self.root.data < node.data else False #root direction.
        if goright == True:
            node2 = self.root.right
        else:
            node2 = self.root.left
        while node2 != None:
            if node2.data >= node.data:
                node2 = node2.left
            else:
                node2 = node2.right
        node2 = node
        if (index+1)==len(self.nlist):
            return
        self.Btree(index+1)"""

root = Node(5)
nlist = [8, 9, 6, 3, 4, 7, 2]
for val in nlist: root.insert(val)
#root.inorderTraversal()
#root.search_node(4)
root.delete_node(8)
root.inorderTraversal()
#root.find_mid()