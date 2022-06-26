from os import *
from sys import *
from collections import *
from math import *

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    temp = head
    counter = 0
    while temp!=None:
        temp = temp.next
        counter+=1
#     print(counter)
    n = counter //2
    temp = head
    while n!=0:
        temp=temp.next
        n-=1
#     print(temp.data)
    return temp
    pass


# or

from os import *
from sys import *
from collections import *
from math import *

'''

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    slow = head
    fast = head
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast= fast.next.next
    return slow
    pass
