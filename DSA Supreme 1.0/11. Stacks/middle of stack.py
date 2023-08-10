class Stack:
    def __init__(self):
        self.head = []
        
    def push(self,data):
        self.head.append(data)
    
    def pop(self):
        self.head.pop()
    
    def size(self):
        return len(self.head)
    
    def top(self):
        return self.head[-1]

def printMiddle(s, size):
    if s.size() == (size//2 +1):
        print(s.top())
        return 
    temp = s.top()
    s.pop()
    printMiddle(s,size)
    s.push(temp)
        
s = Stack()
s.push(10)
s.push(20)
# s.push(30)
# s.push(40)
s.push(50)
printMiddle(s, s.size())
