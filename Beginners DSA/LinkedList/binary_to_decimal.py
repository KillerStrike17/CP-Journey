# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        temp = head
        b_string = ''
        while temp!=None:
            b_string +=str(temp.val)
            temp = temp.next
        # print(b_string)
        return int(b_string,2)