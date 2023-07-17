# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        v1 = 0
        curr = l1
        while curr:
            v1 *= 10
            v1 += curr.val
            curr = curr.next
        v2 = 0
        curr = l2
        while curr:
            v2 *= 10
            v2 += curr.val
            curr = curr.next
        
        v = v1 + v2
        if v == 0:
            return l1
        result = None
        while v:
            result = ListNode(val=v%10, next=result)
            v //= 10
        return result
