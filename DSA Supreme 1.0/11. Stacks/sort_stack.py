class Stack:
    def __init__(self):
        self.head = []
        
    def push(self,data):
        self.head.append(data)
    
    def pop(self):
        return self.head.pop()
    
    def top(self):
        return self.head[-1]
        
    def print(self):
        while self.head !=[]:
            temp = self.pop()
            print(temp)
            self.push(temp)
    def insert_sorted(self,target):
        if self.head == []:
            self.push(target)
            return
        if self.top()<=target:
            self.push(target)
            return
        
        temp = self.pop()
        self.insert_sorted(target)
        self.push(temp)
    
    def sort_stack(self):
        if self.head ==[]:
            return
        else:
            temp = self.pop()
            self.sort_stack()
            self.insert_sorted(temp)
            
        
            
            
            
        

s = Stack()
s.push(50)
s.push(20)
s.push(100)
s.push(40)
s.push(10)
print(s.head)
print(s.sort_stack())
print(s.head)
