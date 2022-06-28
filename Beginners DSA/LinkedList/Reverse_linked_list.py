from os import *
from sys import *
from collections import *
from math import *

"""***************************************************************

    Following is the class structure of the LinkedListNode class:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


*****************************************************************"""


def reverseLinkedList(head):
    # Write your code here.
    if head ==None:
        return None
    curr = head
    prev = None
    n = curr.next
    while curr!=None:
        curr.next = prev
        prev = curr
        curr = n
        if n!=None:
            n = n.next
    return prev
#     pass



