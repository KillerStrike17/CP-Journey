from sys import stdin
import sys


class HashSet:
    
    def __init__(self):
        self.my_arr = [0]*(10**6 +1 )
        # Write your code here.
        pass

    def add(self, key):
        self.my_arr[key] = 1
        # Write your code here.
        # Complete the function.
        pass

    def remove(self, key):
        if self.my_arr[key] == 0:
            return -1
        self.my_arr[key] = 0
        return key
        # Write your code here.
        # Complete the function.
        pass

    def contains(self, key):
        if self.my_arr[key] ==1:
            return True
        return False
        # Write your code here.
        # Complete the function.
        pass


# Main
hashSet = HashSet()
queries = int(input())
while queries:
    values = []
    values = input().split(" ")
    values[0] = int(values[0])
    if values[0] == 1:
        values[1] = int(values[1])
        hashSet.add(values[1])
    elif values[0] == 3:
        values[1] = int(values[1])
        print(hashSet.remove(values[1]))
    elif values[0] == 2:
        values[1] = int(values[1])
        print(hashSet.contains(values[1]))
    queries -= 1




# or