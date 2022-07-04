# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [[root]]
        while queue[-1]:
            queue.append([])
            for node in queue[-2]:
                if node.left:
                    queue[-1].append(node.left)
                if node.right:
                    queue[-1].append(node.right)
        queue.pop()
        return [[node.val for node in level] for level in queue[::-1]]
