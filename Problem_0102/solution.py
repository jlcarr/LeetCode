# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [(root,0)]
        while queue:
            curr,level = queue.pop(0)
            
            if len(result) <= level:
                result.append([])
            result[level].append(curr.val)
            
            if curr.left:
                queue.append((curr.left, level+1))
            if curr.right:
                queue.append((curr.right, level+1))
        
        return result
