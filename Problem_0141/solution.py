# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        tortoise = head
        hare = head.next
        while tortoise != hare:
            if not hare or not hare.next:
                return False
            hare = hare.next.next
            tortoise = tortoise.next
        return True
