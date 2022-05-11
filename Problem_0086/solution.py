# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        less_head, less_tail = None, None
        greater_head, greater_tail = None, None
        while head:
            if head.val < x:
                if not less_head:
                    less_head = head
                    less_tail = head
                else:
                    less_tail.next = head
                    less_tail = less_tail.next
                if greater_tail:
                    greater_tail.next = head.next
            elif head.val >= x:
                if not greater_head:
                    greater_head = head
                    greater_tail = head
                else:
                    greater_tail.next = head
                    greater_tail = greater_tail.next
            head = head.next
        if less_tail:
            less_tail.next = greater_head
            return less_head
        return greater_head
