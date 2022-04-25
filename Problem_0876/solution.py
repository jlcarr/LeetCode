# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        l = head
        while l:
            count += 1
            l = l.next
        middle_index = count//2
        for i in range(middle_index):
            head = head.next
        return head
