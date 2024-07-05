# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [-1, -1]
        pp, p = None, None
        curr = head
        first, last, i = -1, -1, -1
        while curr:
            if pp and ((pp.val < p.val > curr.val) or (pp.val > p.val < curr.val)):
                if first == -1:
                    first = i
                    last = i
                else:
                    if result[0] == -1:
                        result[0] = i-last
                    result = [min(result[0], i-last), i - first]
                    last = i
            #print(curr.val, p.val if p else p, pp.val if pp else pp, i, first, last, result)
            pp = p
            p = curr
            curr = curr.next
            i += 1
        return result

