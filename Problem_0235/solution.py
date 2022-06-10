# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return set()
            found = set()
            if node in [p,q]:
                found.add(node)
            search = dfs(node.left)
            if not isinstance(search, set):
                return search
            found |= search
            if len(found) == 2:
                return node
            search = dfs(node.right)
            if not isinstance(search, set):
                return search
            found |= search
            if len(found) == 2:
                return node
            return found
        return dfs(root)
