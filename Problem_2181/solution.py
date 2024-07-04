# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        currsum = 0
        while curr:
            currsum += curr.val
            if curr.val == 0:
                prev.val = currsum
                prev.next = curr
                if not curr.next:
                    prev.next = None
                prev = curr
                currsum = 0
            curr = curr.next
        prev.next = None
        return head
