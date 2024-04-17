# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ordA = ord('a')
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.result = []
        self.stack = []
        def rec(curr):
            self.stack.append(curr.val+ordA)
            if not curr.left and not curr.right:
                if not self.result or self.stack[::-1] < self.result:
                    self.result = self.stack[::-1]
                self.stack.pop()
                return
            if curr.left:
                rec(curr.left)
            if curr.right:
                rec(curr.right)
            self.stack.pop() 
        rec(root)
        return ''.join(map(chr,self.result))


