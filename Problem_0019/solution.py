# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        first = None
        last = head
        for i in range(n-1):
            last = last.next
            
        while last.next:
            if first:
                first = first.next
            else:
                first = head
            last = last.next
            
        if not first:
            return head.next
        first.next = first.next.next
        return head
