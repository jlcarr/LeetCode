# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return None
        tortoise = head.next
        hare = head.next.next
        while tortoise != hare:
            if hare.next is None or hare.next.next is None:
                return None
            tortoise = tortoise.next
            hare = hare.next.next
            
        hare = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
            
        return hare
        
        # (turns - leadup) % cycle_len = cycle_pos = (2*turns - leadup) % cycle_len
        # 0 = turns % cycle_len
        
