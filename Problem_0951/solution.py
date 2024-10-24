# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return not root1 and not root2
        
        def rec(curr1, curr2):
            if curr1 and curr2:
                print(curr1.val, curr2.val)
            elif not curr1 and curr2:
                print(curr1, curr2.val)
            elif curr1 and not curr2:
                print(curr1.val, curr2)
            elif not curr1 and not curr2:
                print(curr1, curr2)

            if curr1.left and curr2.left and not curr1.right and not curr2.right:
                return (curr1.left.val == curr2.left.val) and rec(curr1.left, curr2.left)
            elif not curr1.left and not curr2.left and curr1.right and curr2.right:
                return (curr1.right.val == curr2.right.val) and rec(curr1.right, curr2.right)
            elif not curr1.left and not curr2.right and curr1.right and curr2.left:
                return (curr1.right.val == curr2.left.val) and rec(curr1.right, curr2.left)
            elif not curr1.right and not curr2.left and curr1.left and curr2.right:
                return (curr1.left.val == curr2.right.val) and rec(curr1.left, curr2.right)
            elif curr1.left and curr2.left and curr1.right and curr2.right:
                if (curr1.left.val == curr2.left.val) and (curr1.right.val == curr2.right.val):
                    return rec(curr1.left, curr2.left) and rec(curr1.right, curr2.right)
                elif (curr1.left.val == curr2.right.val) and (curr1.right.val == curr2.left.val):
                    return rec(curr1.left, curr2.right) and rec(curr1.right, curr2.left)
            elif not curr1.left and not curr2.left and not curr1.right and not curr2.right:
                return True
            return False
        return (root1.val == root2.val) and rec(root1, root2)
