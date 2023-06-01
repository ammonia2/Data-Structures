class Stack:
    
    def __init__(self, size): #constructor, *add list as argument if taking input
        self.stack = [-1]*size #creating a usable list aas stack
        self.size = size
        self.top=-1
        
    def Top(self):  #returns the item at the top of stack
        return self.stack[self.top]  

    def push(self, data):
        if (self.top+1) < self.size:
            self.top+=1
            self.stack[self.top]=data
            #print(self.stack[self.top])
        else:
            print("Stack Overflow")

    def pop(self):
        if self.stack and self.stack[self.top]!=None:
            out = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return out
        else:
            print("stack is empty")

    def print(self):
        item2 = Stack(self.size)
        ret_str = ""
        while self.top>=0:
            temp = self.Top()
            item2.push(temp)
            self.pop()
            ret_str += str(item2.stack[item2.top]) + "-->" if self.top+1<self.size else str(item2.stack[item2.top])
        print(ret_str)

        while item2.top>=0 :  #to avoid '-1' values being added again! 
            temp=item2.Top()
            item2.pop()
            self.push(temp)
        del item2

    def reverse(self):
        item3 = Stack(self.size)
        while self.top>=0:
            temp = self.Top()
            item3.push(temp)
            self.pop()
        self.stack = item3.stack
        self.top = item3.top
        del item3

"""def search_item(list, item): #flawed bec. it takes far too much col.
    index = 0
    itemsearch = None
    while itemsearch != item:
        #print(list[index])
        search = list[index]
        for val in search:
            itemsearch = val
            if itemsearch == item:
                break
        if itemsearch == item:
            break
        index += 1  

    return index   #"*"#"""
    
def checkPrecedence(operator, prevoperator): #dont forget to add "^"
    precedence_l = False
    if operator == ('%') and prevoperator == ('(' or ')' or '/' or '*' or '+' or '-'):  #comparisons   i)top with all below > else True
        precedence_l = False                                                                 #        ii)mid. with below > else True
    elif operator == ('(' or ')' or '/' or '*') and prevoperator == ('+' or '-'):            #       iii)True True
        precedence_l = False
    elif operator == ('+' or '-'):
        precedence_l = True
    return precedence_l

#infix to postfix notation using stack:
def post_conversion(expression):
    operator_stack = Stack(int(len(expression)/2))
    postfix_not, prevpos, out = '', 0, None
    for item in expression:
        unicode = ord(item)
        if unicode >= 97 and unicode <= 122:
            postfix_not += item
        
        else:
            pos = checkPrecedence(item, operator_stack.Top())
            if pos==False:
                operator_stack.push(item)
                if item == ')':
                        while True:
                            out = operator_stack.pop()
                            if out == '(':
                                break
                            if out != ')':
                                postfix_not += str(out)
                            
            else:
                while pos == True and operator_stack.top > -1:
                    out = operator_stack.pop()
                    postfix_not += str(out)         
                    pos = checkPrecedence(item, operator_stack.Top())
                operator_stack.push(item)
                
    while operator_stack.top > -1:
        postfix_not += operator_stack.pop()
    
    print(postfix_not)

#postix to infix procedure:
#1.push opwerands in the stack
#2.remove 2 items from stack if operator comes and place it in between those popped items
#3.add this whole item back in the stack
def inf_conversion(expression):
    op_stack = Stack(3)
    for item in expression:
        unicode = ord(item)
        if unicode >= 97 and unicode <= 122:
            op_stack.push(item)
        else:
            opr1 = op_stack.pop()
            opr2 = op_stack.pop()
            op_stack.push("(" + opr2 + item + opr1 + ")")
    print(op_stack.pop())


#post_conversion('a*b+(c/d)-f')
post_conversion('p+q-r/s')
#inf_conversion("ab*cd/f-+")

# item1 = Stack(6)
# item1.push(4)
# item1.push(5)
# item1.push(6)
# item1.push(7)
# item1.push(8)
# item1.push(10)
# item1.push(11)
# item1.print()
# item1.reverse()
# item1.print()


#code signal**,, leadcode**