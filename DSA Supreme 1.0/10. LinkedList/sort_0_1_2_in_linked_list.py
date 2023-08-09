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
            
def sort_0_1_2(temphead):
    zerohead = Node(-1)
    zerotail = zerohead
    
    onehead = Node(-1)
    onetail = onehead
    
    twohead  =Node(-1)
    twotail = twohead
    
    curr = temphead
    while curr!=None:
        if curr.data == 0:
            temp = curr
            curr = curr.next
            temp.next = None
            zerotail.next= temp 
            zerotail = temp
        elif curr.data == 1:
            temp = curr
            curr = curr.next
            temp.next = None
            onetail.next= temp 
            onetail = temp
        
        else:
            temp = curr
            curr = curr.next
            temp.next = None
            twotail.next= temp 
            twotail = temp 
            
    temp = onehead
    onehead = onehead.next
    temp.next = None
    del temp
    
    temp = twohead
    twohead = twohead.next
    temp.next = None
    del temp
    
    if onehead !=None:
        zerotail.next = onehead
        if twohead !=None:
            onetail.next = twohead
    else:
        if twohead !=None:
            zerotail.next = twohead
    temp = zerohead
    zerohead = zerohead.next
    temp.next= None
    del temp
    
    return zerohead 
    # zerotail.next = onehead.next
    # onetail.next = twohead.next
    
mylist = SingleLinkedList()
mylist.head = Node(0)
e2 = Node(2)
e3 = Node(2)
e4 = Node(1)
e5 = Node(1)
e6 = Node(0)
e7 = Node(2)
e8 = Node(1)
e9 = Node(1)
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
# mylist.listprint()
# removeDuplicates(mylist.head)
mylist.listprint()
temphead= sort_0_1_2(mylist.head)
while temphead!=None:
    print(temphead.data)
    temphead = temphead.next

