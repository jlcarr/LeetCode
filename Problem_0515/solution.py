# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        def rec(currnode, depth):
            if not currnode:
                return
            if len(self.result) == depth:
                self.result.append(currnode.val)
            else:
                 self.result[depth] = max(self.result[depth], currnode.val)
            rec(currnode.left, depth+1)
            rec(currnode.right, depth+1)
        
        rec(root, 0)

        return self.result
