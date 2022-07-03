# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root_val = postorder.pop()
        inorder_index = inorder.index(root_val)
        inorder_left, inorder_right = inorder[:inorder_index], inorder[inorder_index+1:]
        inorder_left_set, inorder_right_set = set(inorder_left), set(inorder_right)
        postorder_left = [v for v in postorder if v in inorder_left_set]
        postorder_right = [v for v in postorder if v in inorder_right_set]
        return TreeNode(val=root_val, left=self.buildTree(inorder_left, postorder_left), right=self.buildTree(inorder_right, postorder_right))
