class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def inceptive_insert(self, data):
        node = Node(data)
        if self.head!=None:
            self.head.prev= node
            node.next = self.head
        self.head = node

    def get_length(self):
        Length = 0
        nextnode = self.head
        while nextnode != None:
            Length += 1
            nextnode = nextnode.next
        return Length

    def printlist(self):
        if self.get_length() == 0:
            print("The list is empty")
            return
        node = self.head
        out_str = ""
        while node != None:
            out_str += str(node.data) + "-->" if node.next else str(node.data)
            node = node.next
        print(out_str)
    
    def end_insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = self.head
        while node.next:
            node  = node.next
        nextnode = Node(data, None, node)
        node.next = nextnode

    def selective_insert(self, data, position):
        if position<1 or position>self.get_length()+1:
            print("Invalid position")
            return
        elif position == 1:
            self.inceptive_insert(data)
            return
        elif position == self.get_length() + 1:
            self.end_insert(data)
            return
        node = self.head
        count = 1 
        while count != position:
            if count == position - 1:
                prev = node    
                next = node.next
                new_node = Node(data, next, node)
                node.next = new_node
                if next:    
                    node = next
                    node.prev = new_node
            node = node.next
            count += 1 

    def reverse_print(self):
        node = self.head
        while node.next:
            node = node.next
        
        out_str = ""
        while node.prev:
            out_str += str(node.data) + '-->' if node.prev else str(node.data)
            node = node.prev
        out_str += str(node.data)
        print(out_str)

    def selective_deletion(self, position):
        if position<1 or position>self.get_length()+1:
            print("Invalid position")
            return
        elif position == 1:
            self.head = self.head.next
            return
        node = self.head 
        count = 1
        while True:
            if count == position-1:
                if node.next.next:
                    node.next = node.next.next
                    prev = node
                    node = node.next
                    node.prev = prev
                else:
                    node.next = None
                break
            node = node.next
            count += 1

    def cumulative_insert(self, data_list):
        for data in data_list:
            self.end_insert(data)

    

    def swap_nodes(self, pos1, pos2): #by swapping pointers
        ploc1, ploc2, node1, node2, prev1, prev2, count, tPrev, tNext = None, None, self.head, self.head, None, None, 1,None, None
        
        while True:  #looping for getting node locations
            if count == pos1-1:
                ploc1 = node1
                node1 = node1.next
                prev1 = node1
                if pos1 > pos2:
                    break
            elif count < pos1:
                node1 = node1.next

            if count == pos2-1:
                ploc2 = node2
                node2 = node2.next
                prev2 = node2
                if pos2 > pos1:
                    break
            elif count < pos2:
                node2 = node2.next

            count += 1

        #swapping next pointers(1):
        if pos1 < pos2:
            if ploc1 != None:
                ploc1.next = node2
            ploc2.next = node1
            #getting node locations early to avoid looping ahead:
            tPrev = ploc2
            tNext = node2.next
            wPrev = ploc1
            wNext = node1.next
            
        elif pos2 < pos1:
            if ploc2 != None:
                ploc2.next = node1
            ploc1.next = node2
            #getting node locations early to avoid looping ahead:
            tPrev = ploc1
            tNext = node1.next
            wPrev = ploc2
            wNext = node2.next
            
            
        #swapping next pointers (2):
        temp = node2.next  
        node2.next = node1.next
        node1.next = temp

        #copying node locaations in case either of them is head:
        node1cc = node1
        node2cc = node2

        #swapping previous pointers(1):
        # node2.prev = ploc1
        # node1.prev = ploc2
        # ploc2.prev=node2
        
        if pos1 < pos2:
            tNext.prev = node1
            node1.prev = tPrev
            wNext.prev = node2
            node2.prev = wPrev

        elif pos2 < pos1:
            tNext.prev = node2
            node2.prev = tPrev
            wNext.prev = node1
            node1.prev = wPrev

        #moving to next location to swap their pointers:
        # node1 = node1.next
        # node2 = node2.next



        #swapping previous pointers(2):
        # if pos2 < pos1:

        #     #if ploc1 != None:
        #     node1 = node1.next
        #     node1.prev = prev2
        #     node2 = node2.next
        #     node2.prev = prev1

        # if pos1 < pos2:
            
        #     #if ploc2 != None:
        #     node2 = node2.next
        #     node2.prev = prev1
        #     node1 = node1.next
        #     node1.prev = prev2

        
        #assigning shifted node as new head (if either was a head)
        if ploc1 == None:
            self.head = node2cc
        elif ploc2 == None:
            self.head = node1cc


dll = Doubly_Linked_List()

dll.end_insert(9)
dll.end_insert(9)
dll.end_insert(5)
dll.end_insert(7)
dll.end_insert(8)
dll.end_insert(9)
#dll.printlist()

dll2 = Doubly_Linked_List()

dll2.cumulative_insert([8, 9, 4, 3])
#dll2.printlist()

def add_list(x1, x2):
    node1 = x1.head
    node2 = x2.head
    while node1.next:
        node1 = node1.next
    while node2.next:
        node2 = node2.next
        
    returndll = Doubly_Linked_List()
    curr_sum, check = 0, False
    
    """while node1.prev: #works the same :)
        if node2.prev == None:
            curr_sum = curr_sum + node1.data + node2.data
            returndll.inceptive_insert(curr_sum%10)
            curr_sum = curr_sum//10
            check = True
            node2.prev = 1

        elif check == False:
            curr_sum = curr_sum + node1.data + node2.data
            returndll.inceptive_insert(curr_sum%10)
            curr_sum = curr_sum//10
            node2 = node2.prev

        node1 = node1.prev
        if check == True:
            curr_sum = curr_sum + node1.data
            returndll.inceptive_insert(curr_sum%10)
            curr_sum = curr_sum//10"""
    
    while node1.prev:  #does the same job :)
        if check == False:
            curr_sum = curr_sum + node1.data + node2.data
            returndll.inceptive_insert(curr_sum%10)
            curr_sum = curr_sum//10
            node2 = node2.prev
            if node2.prev == None:
                node1 = node1.prev
                curr_sum = curr_sum + node1.data + node2.data
                returndll.inceptive_insert(curr_sum%10)
                curr_sum = curr_sum//10
                check = True
                node2.prev = 1
        node1 = node1.prev
        if check == True:
            curr_sum = curr_sum + node1.data
            returndll.inceptive_insert(curr_sum%10)
            curr_sum = curr_sum//10
    if curr_sum>0:    
        returndll.inceptive_insert(curr_sum)
        curr_sum = 0

    returndll.printlist()

add_list(dll, dll2)



