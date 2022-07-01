# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root]]
        depth = 0
        while res[-1]:
            res.append([])
            for node in res[depth][::-1]:
                if depth%2 == 0:
                    if node.right:
                        res[-1].append(node.right)
                    if node.left:
                        res[-1].append(node.left)
                else:
                    if node.left:
                        res[-1].append(node.left)
                    if node.right:
                        res[-1].append(node.right)
            depth += 1
        res.pop()
        return [[n.val for n in row] for row in res]
