class Node:
    def __init__(self,dataval = None) -> None:
        self.dataval = dataval
        self.nextval = None
        
class SingleLinkedList:
    def __init__(self) -> None:
        self.headval = None
        
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
    def insert_at_head(self, dataval):
        newNode = Node(dataval)
        newNode.nextval = self.headval
        self.headval = newNode
    
    def insert_at_tail(self,dataval):
        newNode = Node(dataval)
        if self.headval is None:
            self.headval = newNode
            return
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = newNode
    
    def insert_in_between(self,midnode, newdata):
        if midnode is None:
            return
        
        newNode = Node(newdata)
        newNode.nextval = midnode.nextval
        midnode.nextval = newNode
    
    def findLength(self,head):
        temp = head
        if temp == None:
            return 0
        counter =0
        while temp !=None:
            temp = temp.nextval
            counter +=1
        return counter

    def delete(self,val):
        temp = self.headval
        if temp is not None:
            if temp.dataval == val:
                self.headval = temp.nextval
                temp = None
                return
        
        while(temp is not None):
            if temp.dataval == val:
                break
            prev = temp
            temp = temp.nextval
        
        if temp == None:
            return
        
        prev.nextval = temp.nextval
        temp = None
            
            
            

mylist = SingleLinkedList()
mylist.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
mylist.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

# mylist.listprint()

mylist.insert_at_head("Sun")
# mylist.listprint()

mylist.insert_at_tail("Sat")
# mylist.listprint()

mylist.insert_in_between(e3,"Fri")

print("before")
mylist.listprint()

mylist.delete("Wed")
print("After")
mylist.listprint()