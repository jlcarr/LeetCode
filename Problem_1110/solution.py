# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        def rec(curr, parented=False):
            result = []
            to_del = curr.val in to_delete
            #print(curr.val, to_del, not parented)
            if not to_del and not parented:
                result.append(curr)
            if curr.left:
                result += rec(curr.left, not to_del)
                if curr.left.val in to_delete:
                    curr.left = None
            if curr.right:
                result += rec(curr.right, not to_del)
                if curr.right.val in to_delete:
                    curr.right = None
            return result
        return rec(root)
