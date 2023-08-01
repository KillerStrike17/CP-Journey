class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None
        
class DoubleList:
    def __init__(self):
      self.head = None

    def push(self, newVal):
        newNode = Node(newVal)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
    
    def pop(self):
        start = self.head
        if start is None:
            return
        self.head = start.next
        self.head.prev = None
    
    def remove(self):
        last = self.head
        if last == None:
            return
        if last.next == None:
            self.head = None
            last = None
        while last.next.next is not None:
            last = last.next
        
        last.next = None
    
    def listprint(self, node):
        while node is not None:
            print(node.data)
            last = node,
            node = node.next

    def delete(self, val):
        start = self.head
        if start.data==val:
            self.head = start.next
            self.head.prev = None
            return
        while start.next is not None:
            # print("Here",start.data)
            if start.data == val:
                break
            prev = start
            start = start.next
        #     print("Prev Data:",prev.data,"Start Data:",start.data)
        # print("Prev Data:",prev.data,"Start Data:",start.data)
        prev.next = start.next
        start.prev = prev

    
    def insert(self, prev_node, newVal):
        if prev_node == None:
            return
        newNode = Node(newVal)
        newNode.next = prev_node.next
        prev_node.next = newNode
        newNode.prev = prev_node
        if newNode.next is not None:
            newNode.next.prev = newNode
    
    def append(self, newVal):
        newNode = Node(newVal)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        
        last.next = newNode
        newNode.prev = last
        return
    

        


dllist = DoubleList()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.insert(dllist.head, 13)
dllist.append(45)
print("Before")
dllist.listprint(dllist.head)
# dllist.remove()
# dllist.pop()
dllist.delete(8)
print("After")
dllist.listprint(dllist.head)
