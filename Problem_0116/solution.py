"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        def rec(l, r):
            if not l or not r:
                return
            l.next = r
            rec(l.left, l.right)
            rec(l.right, r.left)
            rec(r.left, r.right)
        rec(root.left, root.right)
        return root
