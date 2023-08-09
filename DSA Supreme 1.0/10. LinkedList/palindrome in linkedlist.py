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
            
    
def reverseLinkedList(head):
    prev = None
    curr = head
    
    while curr !=None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # head = prev
    return prev

def palindrome(head):
    slow = head
    fast = head.next
    while fast !=None:
        fast = fast.next
        if fast !=None:
            fast = fast.next
            slow = slow.next
    
    # print(slow.data)
    # print(fast.data)
    reverseNode_head = reverseLinkedList(slow.next)
    # return reverseNode_head
    slow.next = reverseNode_head
    
    temp1 = head
    temp2 = reverseNode_head
    # return temp1
    # print(temp1.data)
    # print(temp2.data)
    while temp2 !=None and temp1 !=None:
        # print("temp1:",temp1.data)
        # print("temp2:",temp2.data)
        if temp1.data !=temp2.data:
            return False
        # else:
        temp1 = temp1.next
        temp2 = temp2.next
    return True

mylist = SingleLinkedList()
mylist.head = Node(10)
e2 = Node(20)
e3 = Node(30)
e4 = Node(40)
e5 = Node(50)
e6 = Node(40)
e7 = Node(30)
e8 = Node(20)
e9 = Node(10)
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
temphead = palindrome(mylist.head)
print(temphead)
# while temphead !=None:
#     print(temphead.data)
#     temphead = temphead.next
