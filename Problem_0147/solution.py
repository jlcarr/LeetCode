# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head = head
        unsorted_head = head.next
        sorted_head.next = None
        while unsorted_head is not None:
            #print(sorted_head, unsorted_head)
            element = unsorted_head
            unsorted_head = unsorted_head.next

            if element.val < sorted_head.val:
                element.next = sorted_head
                sorted_head = element
            else:
                prev = sorted_head
                curr = sorted_head.next
                while curr is not None and element.val > curr.val:
                    curr = curr.next
                    prev = prev.next
                element.next = curr
                prev.next = element
        return sorted_head


