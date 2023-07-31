class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None
        
class DoubleList:
    def __init__(self):
      self.head = None
