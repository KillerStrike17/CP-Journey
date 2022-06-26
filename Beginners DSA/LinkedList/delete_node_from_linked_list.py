from sys import stdin

# Following is the Node class already written for the Linked List.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def deleteNode(head, pos) :
    # Write your code here.
#     print(head.data)
    counter = 0
    temp = head
    if head ==None:
        print_ll(head)
#     print("head-data",head.data)
    else:
        check = 0
        if pos ==0:
            if temp.next!=None:
                temp2 = temp.next
                temp.data, temp2.data = temp2.data, temp.data
                temp.next =temp2.next
                del temp2
                print_ll(head)
            else:
                head = None
                print_ll(head)
        else:
            while counter<pos-1:
    #             print("data:",temp.data)
    #             print(counter, pos-1)
                if temp.next.next!=None:
                    temp = temp.next
                    counter += 1
                else:
    #                 print("in check")
                    check = 1
                    break

            if check ==1:
                print_ll(head)
            else:
    #             print(temp.data)
                if temp.next.next !=None:
                    temp2 = temp.next
                    temp.next = temp2.next
                    del temp2
                    print_ll(head)
                else:
                    temp.next = None
                    print_ll(head)
#     else:
#         if temp.next != None:
#             temp2 = temp.next
#             temp.data,temp2.data = temp2.data, temp.data
#             temp.next = temp2.next
#             del temp2
#             print_ll(head)
#         else:
# #             temp = 
#             print(temp.data)
#             print(temp.next.data)
            
#         
        
def print_ll(head):
    temp = head
    while(temp!=None):
        print(temp.data,end = " ")
        temp = temp.next

# Taking Input Using Fast I/O.
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



# To print the linked list.
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
