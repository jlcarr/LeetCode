import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

ListNode.__le__ = lambda self,x: self.val <= x.val
ListNode.__lt__ = lambda self,x: self.val < x.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [l for l in lists if l]
        heapq.heapify(lists)
        
        if not lists:
            return None
        
        head = heapq.heappop(lists)
        if head.next:
            heapq.heappush(lists, head.next)
        
        result = head

        while lists:
            next_up = heapq.heappop(lists)
            head.next = next_up
            head = head.next
            if head.next:
                heapq.heappush(lists, head.next)
        return result
