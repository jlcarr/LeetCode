# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        expected = 1
        done = False
        while q:
            nextq = []
            for v in q:
                if v.left:
                    if done:
                        return False
                    nextq.append(v.left)
                else:
                    done = True
                if v.right:
                    if done:
                        return False
                    nextq.append(v.right)
                else:
                    done = True
            print([i.val for i in nextq])
            if nextq and len(q) != expected:
                return False
            expected *= 2
            q = nextq
        return True
        
