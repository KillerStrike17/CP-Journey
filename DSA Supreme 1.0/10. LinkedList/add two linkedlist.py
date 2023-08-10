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

def reverse(head):
    curr = head
    prev = None
    
    while curr!=None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def printList(head):
    temp = head
    while temp!=None:
        print(temp.data)
        temp = temp.next

def add_linkedlist(A,B):
    A_head = reverse(A)
    # printList(A_head)
    
    B_head = reverse(B)
    # printList(B_head)
    
    ans_head = None
    ans_tail = None
    carry = 0
    
    while A_head !=None and B_head !=None:
        
        add = carry + A_head.data + B_head.data
        # print("Here",add)
        digit = add%10
        carry = add//10
        newNode = Node(digit)
        if ans_head == None:
            ans_head = newNode
            ans_tail = newNode
        else:
            ans_tail.next = newNode
            ans_tail = newNode
        A_head = A_head.next
        B_head = B_head.next
        
    while A_head !=None:
        add = carry + A_head.data
        # print(add)
        digit = add%10
        carry = add//10
        newNode = Node(digit)
        ans_tail.next = newNode
        ans_tail = newNode
        A_head = A_head.next 
        
    while B_head !=None:
        add = carry + B_head.data
        # print(add)
        digit = add%10
        carry = add//10
        newNode = Node(digit)
        ans_tail.next = newNode
        ans_tail = newNode
        B_head = B_head.next
        
    while carry!=0:
        sum = carry
        digit = sum%10
        carry = sum//10
        newNode = Node(digit)
        ans_tail.next = newNode
        ans_tail = newNode
        
    ans = reverse(ans_head)
    return ans
    

A = SingleLinkedList()
A.head = Node(9)
A2 = Node(9)
# A3 = Node(3)
A.head.next = A2
# A2.next = A3

B = SingleLinkedList()
B.head = Node(9)
B2 = Node(9)
B.head.next = B2

ans = add_linkedlist(A.head,B.head)
printList(ans)
    

        
    
