# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        result = head.next
        prev = None
        while head and head.next:
            if prev:
                prev.next = head.next
            temp = head.next
            head.next = head.next.next
            temp.next = head
            prev = head
            head = head.next
        return result
