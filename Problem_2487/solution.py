# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        # reverse first
        curr = head
        head = None
        while curr:
            temp = curr.next
            curr.next = head
            head = curr
            curr = temp

        # delete descending
        curr = head
        while curr and curr.next:
            if curr.val > curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        # reverse first
        curr = head
        head = None
        while curr:
            temp = curr.next
            curr.next = head
            head = curr
            curr = temp
        
        return head
