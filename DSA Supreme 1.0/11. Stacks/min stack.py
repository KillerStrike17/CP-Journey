class Stack:
    def __init__(self):
        self.head = []
        self.min = 999999999999999
        
    def push(self,data):
        if data<self.min:
            self.min = data
        self.head.append(data)
    
    def pop(self):
        return self.head.pop()
    
    def top(self):
        return self.head[-1]
    
    def getmin(self):
        return self.min

            
            
            
        

s = Stack()
s.push(50)
s.push(20)
s.push(100)
s.push(40)
s.push(10)
print(s.head)
print(s.getmin())
