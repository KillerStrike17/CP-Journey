class Node:
    def __init__(self,dataval = None) -> None:
        self.data = dataval
        self.next = None
        
class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    

def checkForLoop(head):
    if head ==None:
        return
    slow = head
    fast = head
    while fast!=None:
        fast = fast.next
        if fast!=None:
            fast = fast.next
            slow = slow.next
        if slow == fast:
            return True
    return False
    
mylist = SingleLinkedList()
mylist.head = Node(10)
e2 = Node(20)
e3 = Node(30)
e4 = Node(40)
e5 = Node(50)
e6 = Node(60)
e7 = Node(70)
e8 = Node(80)
e9 = Node(90)
mylist.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
e7.next = e8
e8.next = e9
# e9.next = e5
print(checkForLoop(mylist.head))
