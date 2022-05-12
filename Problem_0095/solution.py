# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def rec(vals):
            if not vals:
                return []
            if len(vals) == 1:
                return [TreeNode(vals[0], None, None)]
            
            result = []
            for v in vals:
                left_vals = [i for i in vals if i < v]
                right_vals = [i for i in vals if i > v]
                
                # split
                sub_lefts = rec(left_vals)
                sub_rights = rec(right_vals)
                for l in sub_lefts:
                    for r in sub_rights:
                        result.append(TreeNode(v, l, r))
                
                if not sub_lefts:
                    for r in sub_rights:
                        result.append(TreeNode(v, None, r))
                if not sub_rights:
                    for l in sub_lefts:
                        result.append(TreeNode(v, l, None))
                
            return result
        return rec(list(range(1,n+1)))
