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
    def push_brack(self,string):
        for data in string:
            if data =='{' or data =="[" or data =='(':
                self.push(data)
            else:
                if self.head!= []:
                    top_val = self.top()
                    if data ==')' and top_val =='(':
                        self.pop()
                    elif data =='}' and top_val =='{':
                        self.pop()
                    elif data ==']' and top_val =='[':
                        self.pop()
                    else:
                        return False
                else:
                    return False
        if self.head == []:
            return True
        else:
            return False
                    
        
        # return True

s = Stack()
mystring = ['[',']','{','}',')']
print(s.push_brack(mystring))

# s.push_at_bottom(60)
# print(s.head)
# s.reverse_stack()
# print(s.head)
# s.print()
