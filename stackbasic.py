Top = -1
Max = 5

def Initialise():
    global Top
    Top = -1

def Push(myStack):
    global Top
    if Top == Max-1:
        print("Stack full!")
    else:
        Top += 1
        char = input("Enter character:")
        myStack[Top] = char
        print("Added ", char)

def Pop(myStack):
    global Top
    if Top == -1:
        print("Stack is empty")
    else:
        print(myStack[Top], " removed ")
        Top += -1

def Traverse(myStack):
    global Top
    count = Top
    if count == -1:
        print("stack is empty")
    while count > -1:
        print(myStack[count])
        count += -1

def Search(myStack, char):
    global Top
    count = Top
    found = False
    while count > -1:
        if myStack[count] == char:
            print("Found ", char, " at position ", count)
            found = True 
        count += -1
    if not found:
        print("sesrch failed ")

def main():
    myStack = [0,0,0,0,0]
    Initialise()
    choice = 0
    while choice != 6:
        print("1 Initialise the stack")
        print("2 Push into stack")
        print("3 Remove from stack")
        print("4 Print contents")
        print("5 Search stack")
        print("6 Quit")
        choice = int(input("Enter the choice: "))
        
        if choice == 1:
            Initialise()
        elif choice == 2:
            Push(myStack)
        elif choice == 3:
            Pop(myStack)
        elif choice == 4:
            Traverse(myStack)
        elif choice == 5:
            searchchar = input("Enter character to be searched: ")
            Search(myStack, searchchar)
        elif choice == 6:
            print("Closed")

main()