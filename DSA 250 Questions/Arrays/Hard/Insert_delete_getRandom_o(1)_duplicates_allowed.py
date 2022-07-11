import random
class RandomizedCollection:

    def __init__(self):
        self.myList = []
        

    def insert(self, val: int) -> bool:
        if val in self.myList:
            self.myList.append(val)
            return False
        else:
            self.myList.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.myList:
            self.myList.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.myList)