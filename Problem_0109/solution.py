# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # convert to list
        vals = []
        while head is not None:
            vals.append(head.val)
            head = head.next
        
        def rec(vals):
            if not vals:
                return None
            l = len(vals)
            v = vals[l//2]
            return TreeNode(val=v, left=rec(vals[:l//2]), right=rec(vals[l//2+1:]))
        
        return rec(vals)
