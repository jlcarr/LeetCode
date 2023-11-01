# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.modes = []
        self.count = 0
        self.lastseen = None
        self.last_count = 0
        def inorder(curr):
            if curr.left:
                inorder(curr.left)
            if curr.val == self.lastseen:
                self.last_count += 1
            else:
                self.lastseen = curr.val
                self.last_count = 1
            if self.last_count == self.count:
                self.modes.append(self.lastseen)
            if self.last_count > self.count:
                self.modes = [self.lastseen]
                self.count = self.last_count
            if curr.right:
                inorder(curr.right)
        inorder(root)
        return self.modes
