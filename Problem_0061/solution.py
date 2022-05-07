# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        # count the number of nodes in the list
        l = 1
        curr = head
        while curr.next:
            curr = curr.next
            l += 1
        # and make sure we only rotate once.
        k %= l
        
        # loop it ahead of time, helps with edge cases
        curr.next = head
        
        for i in range(l-k):
            curr = curr.next
        
        new_head = curr.next
        curr.next = None
        return new_head
        
        
        
