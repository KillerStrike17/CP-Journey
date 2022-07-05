import random
class RandomizedSet:

    def __init__(self):
        self.RSet = set()
        

    def insert(self, val: int) -> bool:
        if val in self.RSet:
            return False
        else:
            self.RSet.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.RSet:
            self.RSet.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        x = list(self.RSet)
        # print(x)
        if len(x)>0:
            return random.sample(x,1)[0]
        return self.RSet
        