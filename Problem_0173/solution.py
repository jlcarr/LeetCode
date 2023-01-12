# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._fillstack(root)
        

    def next(self) -> int:
        v = self.stack.pop()
        if v.right:
            self._fillstack(v.right)
        return v.val
        

    def hasNext(self) -> bool:
        return bool(self.stack)
        

    def _fillstack(self, curr):
        while curr:
            self.stack.append(curr)
            curr = curr.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
