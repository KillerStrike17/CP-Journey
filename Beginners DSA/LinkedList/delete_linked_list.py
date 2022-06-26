from os import *
from sys import *
from collections import *
from math import *

# Following is the List Node Class
class LinkedListNode:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def deleteNode(node):
    # Write your code here.
    if node.next == None:
        del node
    else:
        node.data, node.next.data =  node.next.data,node.data
        temp = node.next
        node.next = temp.next
        del temp
    pass