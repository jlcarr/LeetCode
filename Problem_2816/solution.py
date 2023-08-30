# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        v = 0
        curr = head
        while curr:
            v *= 10
            v += curr.val
            curr = curr.next
        
        if v == 0:
            return head
        
        v *= 2
        result = None
        while v > 0:
            newNode = ListNode(val=v%10, next=result)
            result = newNode
            v //= 10
        return result
