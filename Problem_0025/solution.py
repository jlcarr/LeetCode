# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseFirstK(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result_head = None
        result_tail = head
        curr = head
        
        i = 0
        while i < k: # perform the reversing
            i += 1
            proc = curr.next
            curr.next = result_head
            result_head = curr
            if not proc:
                break
            curr = proc
        
        return result_head, result_tail, i, proc
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # first group (guarunteed to exist completely)
        result, tail, group_len, head = self.reverseFirstK(head, k)
        #print(result.val, head.val)
        
        while head:
            group_head, group_tail, group_len, head = self.reverseFirstK(head, k)
            if group_len < k:
                group_head, group_tail, group_len, head = self.reverseFirstK(group_head, k)
                tail.next = group_head
                return result
            tail.next = group_head
            tail = group_tail
            
        return result
