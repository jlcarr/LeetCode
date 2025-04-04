# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(curr, depth):
            # depth lca
            if not curr.left and not curr.right:
                return depth, curr
            elif curr.left and not curr.right:
                return rec(curr.left, depth+1)
            elif not curr.left and curr.right:
                return rec(curr.right, depth+1)
            else:
                l, llca = rec(curr.left, depth+1)
                r, rlca = rec(curr.right, depth+1)
                if l > r:
                    return l, llca
                elif r > l:
                    return r, rlca
                else:
                    return l, curr
        #print(rec(root, 0)[-1])
        return rec(root, 0)[-1]


