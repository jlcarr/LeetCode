# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        new_tail = head
        new_head = head
        while new_tail.next:
            temp = new_tail.next
            new_tail.next = temp.next
            temp.next = new_head
            new_head = temp
        return new_head
