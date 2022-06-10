# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        node = TreeNode(val=preorder[0])
        
        left_inorder = []
        while inorder[0] != preorder[0]:
            left_inorder.append(inorder.pop(0))
            
        # remove root
        inorder.pop(0)
        preorder.pop(0)
        
        left_set = set(left_inorder)
        left_preorder = []
        while preorder and preorder[0] in left_set:
            left_preorder.append(preorder.pop(0))
            
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(preorder, inorder)
        
        return node
