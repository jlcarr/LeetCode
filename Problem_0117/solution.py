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
    def connect(self, root: 'Node') -> 'Node':
        level_start = root
        while level_start:
            curr = level_start
            level_start = None
            level_end = None
            while curr:
                if not level_start:
                    if curr.left:
                        level_start = curr.left
                        level_end = level_start
                        if curr.right:
                            level_end.next = curr.right
                            level_end = level_end.next
                    elif curr.right:
                        level_start = curr.right
                        level_end = level_start
                else:
                    if curr.left:
                        level_end.next = curr.left
                        level_end = level_end.next
                    if curr.right:
                        level_end.next = curr.right
                        level_end = level_end.next
                curr = curr.next
        return root
                
