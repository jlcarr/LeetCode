# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        def rec(node, depth=0):
            if not node:
                return
            if len(res) == depth:
                res.append(node.val)
            rec(node.right, depth=depth+1)
            rec(node.left, depth=depth+1)
        rec(root)
        return res
                
