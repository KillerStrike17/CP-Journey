class Stack:
    def __init__(self,n):
        self.head = []
        for _ in range(n):
            self.head.append(None)
        self.top1 = 0
        self.top2 = len(self.head)-1
        # s
        
    def push1(self,data):
        if self.top2 - self.top1 ==1:
            print("overflow")
        else:
            
            self.head[self.top1] = data
            self.top1+=1
            
    def push2(self,data):
        if self.top2 - self.top1 ==1:
            print("overflow")
        else:
            
            self.head[self.top2] = data
            self.top2 -=1
    
    def pop2(self):
        self.head[self.top2] == None
        self.top2+=1
    
    def pop1(self):
        self.head[top1] == None
        self.top1-=1
        
    def print_arr(self):
        for _ in self.head:
            print(_,end=" ")
        print()

s = Stack(10)
s.push1(1)
s.print_arr()
s.push2(2)
s.print_arr()
s.push1(3)
s.print_arr()
s.push1(4)
s.print_arr()
s.push2(5)
s.print_arr()
s.push2(6)
