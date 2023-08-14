class Stack:
    def __init__(self):
        self.head = []
        
    def push(self,data):
        self.head.append(data)
    
    def pop(self):
        return self.head.pop()
    def push_at_bottom(self,data):
        if self.head == []:
            self.push(data)
            return
            # self.head
        temp = self.pop()
        self.push_at_bottom(data)
        self.push(temp)
        
    def print(self):
        while self.head !=[]:
            temp = self.pop()
            print(temp)
            self.push(temp)
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push_at_bottom(60)
print(s.head)
# s.print()
