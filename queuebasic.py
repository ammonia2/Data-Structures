Head = 0
Tail = -1
Size = 0

def Initialise():
    global Head, Tail, Size
    Head = 0
    Tail = -1
    Size = 0

def Enqueue(queue):
    global Tail, Size
    if Size == 5:
        print("Queue overflow.")
    else:
        Size += 1
        Tail += 1
        if Tail >= 5:
            Tail = 0
        char = input("Enter a character: ")
        queue[Tail] = char
        print("Added ", char)


def Dequeue(queue):
    global Head, Size
    if Size == 0:
        print("Queue empty!")
    else:
        print(queue[Head], " was removed from the queue!")
        Head += 1
        Size += -1
        if Head >= 5:
            Head = 0

def Traverse(queue):
    global Head, Tail, Size
    count = Head
    counted = 0
    stringToPrint = "[Front]<- "
    print("Traversing queue...")
    while counted != Size:
        stringToPrint = stringToPrint + queue[count] + " "
        count += 1
        counted += 1
        if count >= 5:
            count = 0
    if Size == 0:
        print("Nothing to print, queue empty!")
    else:
        stringToPrint = stringToPrint + "<-[Back]"
        print(stringToPrint)
        

def Search(queue, Char):
    global Head, Size
    count = Head
    counted = 0
    found = False
    while counted != Size:
        count += 1
        counted += 1
        if count >= 5:
            count = 0
        if queue[count] == Char:
            found = True
            print("Found ", Char, " in the queue!")
    if found == False:
        print("Couldn't find ", Char, " in the queue!")


def main():
    queue = [0,0,0,0,0]
    Initialise()
    choice = 0
    while choice != 6:
        print("\n************************************************")
        print("1 Initialise the queue")
        print("2 Enqueue")
        print("3 Dequeue")
        print("4 Print the contents of the queue")
        print("5 Search the queue")
        print("6 Quit")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            Initialise()
        elif choice == 2:
            Enqueue(queue)
        elif choice == 3:
            Dequeue(queue)
        elif choice == 4:
            Traverse(queue)
        elif choice == 5:
            char_to_search = input("Enter the character to be searched: ")
            Search(queue, char_to_search)
        elif choice == 6:
            print('Closed')

main()