# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # find length
        l = 1
        curr = head
        while curr.next:
            curr = curr.next
            l += 1
        # use length to find mid
        curr = head
        for i in range(l//2-1):
            curr = curr.next
        next_head = curr.next
        curr.next = None

        # recuse
        sorted_first = self.sortList(head)
        sorted_second = self.sortList(next_head)
        #print(sorted_first,sorted_second)

        # merge
        #first define the result head and tail
        if sorted_first.val < sorted_second.val:
            result = sorted_first
            sorted_first = sorted_first.next
        else:
            result = sorted_second
            sorted_second = sorted_second.next
        tail = result
        # merge the two
        while sorted_first and sorted_second:
            if sorted_first.val < sorted_second.val:
                tail.next = sorted_first
                sorted_first = sorted_first.next
            else:
                tail.next = sorted_second
                sorted_second = sorted_second.next
            tail = tail.next
        # finish remianing
        if sorted_first:
            tail.next = sorted_first
        if sorted_second:
            tail.next = sorted_second
        # return
        return result
            
