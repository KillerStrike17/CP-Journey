class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
        
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.data) + "->"
            cur = cur.next
        return out[:-2]
    
    def peek(self):
        if self.isEmpty():
            print("Is Empty")
        return self.head.next.value
    
    def push(self,val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size +=1
    
    def pop(self):
        if self.isEmpty():
            print("Stack empty")
            return
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -=1
        return remove.data

stack = Stack()
# stack.head = Node(0)
for i in range(1, 11):
    stack.push(i)
    
print(f"Stack: {stack}")

for _ in range(1, 6):
    remove = stack.pop()
    print(f"Pop: {remove}")
print(f"Stack: {stack}")
        
    
