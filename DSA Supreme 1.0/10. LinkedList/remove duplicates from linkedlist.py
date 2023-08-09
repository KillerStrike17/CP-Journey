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
            
def removeDuplicates(temphead):
    head = temphead
    if head == None or head.next == None:
        return head
    while head!=None and head.next!=None:
        if head.data ==head.next.data:
            head.next = head.next.next
        else:
            head = head.next

            
    
mylist = SingleLinkedList()
mylist.head = Node(10)
e2 = Node(20)
e3 = Node(20)
e4 = Node(40)
e5 = Node(40)
e6 = Node(40)
e7 = Node(70)
e8 = Node(80)
e9 = Node(80)
mylist.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
e7.next = e8
e8.next = e9
# e9.next = e5
# RemoveLoop(mylist.head)
mylist.listprint()
removeDuplicates(mylist.head)
mylist.listprint()

