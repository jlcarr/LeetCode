# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        curr = head
        while curr is not None:
            l += 1
            curr = curr.next
        
        subdiv = l // k
        submod = l % k

        returnval = []
        curr = head
        for ik in range(k):
            if not curr:
                returnval.append(None)
                continue
            returnval.append(curr)

            for il in range(subdiv-1):
                curr = curr.next
            if subdiv > 0 and ik < submod:
                curr = curr.next
            prev = curr
            if curr is not None:
                curr = curr.next
                prev.next = None
        
        return returnval
