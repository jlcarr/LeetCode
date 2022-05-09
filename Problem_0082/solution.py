# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr.next = curr.next.next
                if not prev:
                    head = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
        
